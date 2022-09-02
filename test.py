import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# REQUIREMENTS: https://pixeltree.notion.site/City-Council-Scraping-34a2f5a24d59400faf9a128f2653ebf2
# Meeting Minutes Directory: https://pub-calgary.escribemeetings.com

# TODO
# 1. JSON Structure, serialize
# 2. Complete the rest of the fields
# 3. Classify using spaCy

# Object to be seriliazed
JSON_obj = {}

URL = "https://pub-calgary.escribemeetings.com/Meeting.aspx?Id=9a27aea6-df27-4322-907f-164396fcf3b0&Agenda=PostMinutes&lang=English"
page = requests.get(URL)
o = urlparse(URL)
query = parse_qs(o.query)

JSON_obj["meeting_id"] = query["Id"][0]

# Complete HTML File
soup = BeautifulSoup(page.content, "html.parser")

# Most of the page content is found in this container
page_content = soup.find(id="package-container")

# MM Header
agenda_header = page_content.find("header", class_="AgendaHeader")

## Header information

# Get the Agenda Header
JSON_obj["agenda_header_subtitle"] = agenda_header.find("p", class_="AgendaHeaderSubTitle").text

# Get the start time
JSON_obj["start_time"] = agenda_header.find("time").text

# Get the location
JSON_obj["location"] = agenda_header_subtitle = agenda_header.find("div", class_="Value LocationValue").text ### This does not get all location info

attendance_table = agenda_header.find("div", class_="AgendaHeaderAttendanceTable").find_all("div")
# Get the attendence (seperated by who can and can't vote)
present = [x.text for x in attendance_table[2].find_all("li")]
also_present = [x.text for x in attendance_table[5].find_all("li")]


JSON_obj["attendance"] = {'present': present, 'also_present': also_present}


# MM Body
agenda_items = page_content.find("div", class_="AgendaItems")


## Body information
agenda_item_containers = agenda_items.find_all("div", class_="AgendaItemContainer indent")

# roll_call = agenda_item_containers[0].find_all("p", class_="Body1")

# JSON_obj["roll_call"] = roll_call[2].text.rstrip('.').split(', and ')


agenda_item_containers = agenda_items.children


g = 1
for agenda_item in agenda_item_containers:
    titles = [x.text for x in agenda_item.find_all("div", class_="AgendaItemTitle")]
    
    # motions = agenda_item.find_all("ul", class_="AgendaItemMotions")

    motions = agenda_item.find_all("ul", class_="AgendaItemMotions")

    print(g)

    if motions == None:
        print("No motions")
    else:
        h = 1
        for motion in motions:
            print(str(g) + '.' + str(h))

            # Get the motion title
            motion_titles = [x.parent.parent.parent.parent for x in motion.find_all("div", class_="MotionText RichText")]
            motion_titles = [x.find("div", class_="AgendaItemTitle").text.strip() for x in motion_titles]

            moved_by_list = [x.find("span", class_="Value") for x in motion.find_all("div", class_="MovedBy")]
            moved_by_list  = [x.text for x in moved_by_list]

            # Motion description
            motion_description_list = [x.text for x in motion.find_all("div", class_="MotionText RichText")]

            # Motion result
            motion_result_list = [x.text for x in motion.find_all("div", class_="MotionResult")]

            # Motion votes
            motion_votes_list = [x.text[x.text.find(')') + 1:].split(', and ') for x in motion.find_all("table", class_="MotionVoters")]

            # Motion Attachments

            print(motion_titles) # title
            # print("Moved by: " + str(moved_by_list)) # Moved by
            print(motion_description_list) # Other details
            # print("Result: " + str(motion_result_list)) # Result
            # print("Votes: " + str(motion_votes_list)) # Votes
            # # attachment links
            print()
            h+=1


    # item_children = agenda_item.find_all(attrs={'class': None})

    # print(len(item_children))

    # for child in item_children:
    #     print(child.find("div", class_="AgendaItemTitle"))





    print('-----------------------------------\n\n\n')
    g+=1


# # Horizontal
# while(child_node != None):
#     print(child_node)
#     child_node = child_node.next_sibling


# # Depth
# while(child != None):
#     print(agenda_item)
#     agenda_item = agenda_item.child






