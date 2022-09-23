import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

from utils import isValidURL

import json
import sys
import os

# REQUIREMENTS: https://pixeltree.notion.site/City-Council-Scraping-34a2f5a24d59400faf9a128f2653ebf2
# Meeting Minutes Directory: https://pub-calgary.escribemeetings.com

# INPUT (arg 1): Valid URL pointing to meeting minutes. Needs to be wrapped in quotes
# OPTIONAL INPUT (arg 2): Output directory
# OUTPUT: JSON document containing required information scraped from input URL

# Debug mode
DEBUG = False

def minutes_scraper(URL=""):
    if not isValidURL(URL):
        print("Invalid or missing URL input")
        print("Please enter a URL now:")

        return "Invalid URL"

    # Get output directory
    out_dir = ""
    out_dir = os.getcwd()

    ###

    # Object to be seriliazed
    JSON_obj = {}

    # Get meeting ID
    page = requests.get(URL)
    o = urlparse(URL)
    query = parse_qs(o.query)

    JSON_obj["meeting_id"] = query["Id"][0]

    # Complete HTML File
    soup = BeautifulSoup(page.content, "html.parser")

    # Most of the page content is found in this container
    page_content = soup.find(id="package-container")

    ###

    # MM Header
    agenda_header = page_content.find("header", class_="AgendaHeader")

    ## Header information

    # Get the Agenda Header
    try: 
        JSON_obj["agenda_header_subtitle"] = agenda_header.find("p", class_="AgendaHeaderSubTitle").text
    except AttributeError:
        JSON_obj["agenda_header_subtitle"] = ""


    # Get the start time
    JSON_obj["start_time"] = agenda_header.find("time").text

    # Get the location
    try:
        JSON_obj["location"] = agenda_header_subtitle = agenda_header.find("div", class_="Value LocationValue").text ### This does not get all location info
    except AttributeError:
        JSON_obj["location"] = ""

    # Get the attendence (seperated by who can and can't vote)
    attendance_table = agenda_header.find(class_="AgendaHeaderAttendanceTable").find_all("div")
    try:
        present = [x.text for x in attendance_table[2].find_all("li")]
    except IndexError:
        present = []

    try:
        also_present = [x.text for x in attendance_table[5].find_all("li")]
    except IndexError:
        also_present = []

    JSON_obj["attendance"] = {'present': present, 'also_present': also_present}

    ###

    # MM Body
    agenda_items = page_content.find("div", class_="AgendaItems")

    ## Body information

    # Get item containers
    agenda_item_containers = agenda_items.find_all("div", class_="AgendaItemContainer indent")

    # Get roll call
    try:
        roll_call = agenda_item_containers[0].find_all("p", class_="Body1")
        JSON_obj["roll_call"] = roll_call[2].text.rstrip('.').replace(', and ', ', ').split(', ')
    except IndexError:
        JSON_obj["roll_call"] = []

    if DEBUG:
        print(JSON_obj["roll_call"])

    # Get generator of item containers
    agenda_item_containers = agenda_items.children

    item_number = 1
    for agenda_item in agenda_item_containers:

        # Get titles
        titles = [x.text for x in agenda_item.find_all("div", class_="AgendaItemTitle")]
        
        # Get each motion in each item
        motions = agenda_item.find_all("ul", class_="AgendaItemMotions")

        if DEBUG:
            print(item_number)

        if motions != None:
            item_sub_number = 1

            for motion in motions:

                # Dictionary to store all motion info
                motion_obj = {}

                if DEBUG:
                    print(str(item_number) + '.' + str(item_sub_number))

                # Place "anchor"
                motion_anchor = [x.parent.parent.parent.parent for x in motion.find_all("div", class_="MotionText RichText")]

                # Get motion title
                motion_titles = [x.find("div", class_="AgendaItemTitle").text.strip() for x in motion_anchor]

                # Get list of who the motion is moved by
                moved_by_list = [x.find("span", class_="Value") for x in motion.find_all("div", class_="MovedBy")]
                moved_by_list  = [x.text for x in moved_by_list]

                # Get motion description
                motion_description_list = [x.text for x in motion.find_all("div", class_="MotionText RichText")]

                # Get motion result
                motion_result_list = [x.text for x in motion.find_all("div", class_="MotionResult")]

                # Get motion votes
                motion_votes_list = [x.text[x.text.find(')') + 1:].split(', and ') for x in motion.find_all("table", class_="MotionVoters")]

                # Get motion attachments
                motion_attachments_list = [x.find_all("a", class_="Link") for x in motion_anchor]
                motion_attachments_list_names = []
                motion_attachments_list_links = []
                for x in motion_attachments_list:
                    motion_attachments_list_names.append([y.text for y in x]) # ?
                    motion_attachments_list_links.append([y['href'] for y in x])

                motion_obj["titles"] = motion_titles
                motion_obj["moved_by"] = moved_by_list
                motion_obj["details"] = motion_description_list
                motion_obj["results"] = motion_result_list
                motion_obj["votes"] = motion_votes_list
                motion_obj['attachment_names'] = motion_attachments_list_names[0]
                motion_obj['attachment_links'] = motion_attachments_list_links[0]


                if DEBUG:
                    print(str(item_number) + '.' + str(item_sub_number))
                    print(motion_titles) # title
                    print("Moved by: " + str(moved_by_list)) # Moved by
                    print(motion_description_list) # Other details
                    print("Result: " + str(motion_result_list)) # Result
                    print("Votes: " + str(motion_votes_list)) # Votes
                    print(motion_attachments_list_names[0]) # attachment names
                    print(motion_attachments_list_links[0]) # attachment links
                    print()

                # Append to JSON object
                JSON_obj[f'{item_number}.{item_sub_number}'] = motion_obj

                item_sub_number+=1

        if DEBUG:
            print('-----------------------------------\n\n\n')

        item_number+=1


    # # Serialize and write to "meeting_minutes.json"
    # with open(f"{out_dir}/meeting_minutes.json", "w") as out:
    #     json.dump(JSON_obj, out, indent=4)

    # Add this to data base
    
    return JSON_obj