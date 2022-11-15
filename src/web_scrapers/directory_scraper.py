from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep
from datetime import date as dt
import os

from ..utils.db_connect import connectMongo
from .meeting_minutes_scraper import minutes_scraper



# To run this script use:
# python -m src.web_scrapers.directory_scraper
# from the root directory

def directory_scraper(URL="https://pub-calgary.escribemeetings.com/?Year=2022", scrape_each_meeting=False, upload_to_db=False, database="Calgary"):

    if int(scrape_each_meeting) + int(upload_to_db) == 1:
        print("Please enter a valid set of arguments")
        return "Invalid arguments"

    # connect to the database on true
    if upload_to_db:
        client = connectMongo()
        db = client[database]
        today = dt.today().strftime('%Y-%m-%d')

    # initialize webdriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    # el = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.panel-contents.MeetingTypeContainer")))

    directory_URL = URL

    driver.get(directory_URL) # open url

    past_meeting_categories_container = driver.find_element(By.ID, "PastMeetingTypesAccordian")

    past_meeting_category = past_meeting_categories_container.find_elements(By.CLASS_NAME, "MeetingTypeList")

    for category in past_meeting_category:
        if category.is_displayed():
            category.find_element(By.TAG_NAME, "a").click()

            wait.until(EC.url_contains("&Expanded="))

            # wait.until(lambda d: 'Loaded' in el.get_attribute('class'))
            sleep(3) # wait for resources to load

            meetings_container = category.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div")

            meetings = meetings_container.find_elements(By.XPATH, "*") # Find direct child elements

            for meeting in meetings:
                if meeting.is_displayed():
                    title = meeting.find_element(By.CLASS_NAME, "meeting-title-heading").text
                    date = meeting.find_element(By.CLASS_NAME, "meeting-date").text

                    print(f"Working on {title} from {date}")

                    with open(f'log_{today}.txt', 'a') as f:
                        f.write(f"Working on {title} from {date}")

                    try:
                        resources = meeting.find_element(By.CLASS_NAME, "resource-list").find_elements(By.CLASS_NAME, "packageType")
                    except NoSuchElementException:
                        resources = [] # continue; no resources

                    for resource in resources:
                        try:
                            resource_name = resource.find_element(By.CLASS_NAME, "packageName").text
                        except NoSuchElementException:
                            resource_name = "No name" # continue; no name

                        if resource_name == "Minutes":
                            resource_link = resource.find_element(By.TAG_NAME, "a").get_attribute("href")

                            print(f"Found {resource_name}: {resource_link}")

                            with open(f'log_{today}.txt', 'a') as f:
                                f.write(f"Found {resource_name}: {resource_link}")

                            if scrape_each_meeting:
                                print(f"scraping: {resource_link}")

                                with open(f'log_{today}.txt', 'a') as f:
                                    f.write(f"scraping: {resource_link}")
                                
                                try:
                                    meeting_obj = minutes_scraper(resource_link)
                                except Exception as e:
                                    print(f"Error scraping {resource_link}: {e}")

                                    with open(f'log_{today}.txt', 'a') as f:
                                        f.write(f"Error scraping {resource_link}: {e}")

                                    continue

                                if upload_to_db:

                                    print(f"upserting to db: {resource_link}")

                                    with open(f'log_{today}.txt', 'a') as f:
                                        f.write(f"upserting to db: {resource_link}")
                    
                                    db.escribe_meetings.update_one({"meeting_id": meeting_obj["meeting_id"]}, {"$set": meeting_obj}, upsert=True)

    driver.quit() # kill web driver

    log = open(f"log_{today}.txt", "r")

    num_logs_today = db.escribe_meetings.count_documents({"date": today})

    db.logs.insert_one({"date": today, "log_number": num_logs_today, "log":  log.read() })

    os.remove(f"log_{today}.txt")

directory_scraper(scrape_each_meeting=True, upload_to_db=True)