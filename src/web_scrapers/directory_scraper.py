from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

import re

from time import sleep


# def find_meeting_urls(URL): # bs4
#     page = requests.get(URL)

#     soup = BeautifulSoup(page.content, "html.parser")

#     page_content = soup.find(id="PastMeetingTypesAccordian")

#     o = urlparse(URL)
#     query = parse_qs(o.query)

#     year = query["Year"][0]
#     title = query["Expanded"][0].replace(" ", "+")

#     # meeting_URL = f"https://pub-calgary.escribemeetings.com/meetingscalendarview.aspx?Year={year}&Expanded={title}"
#     meeting_URL = f"https://pub-calgary.escribemeetings.com:443/meetingscalendarview.aspx?Year={year}&Expanded={title}"

#     calendarview_link = page_content.find("a", href=meeting_URL)

#     print(calendarview_link.parent)



#     # items = calendarview_link.next_sibling.next_sibling

#     # print(items.prettify())

#     # print(meetings_group.next_sibling.next_sibling.prettify())

#     # print(meetings_group.prettify())




#     # print(meetings)

#     # print(page_content)


# find_meeting_urls("https://pub-calgary.escribemeetings.com/?Year=2022&Expanded=Combined%20Meeting%20of%20Council")


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

el = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.panel-contents.MeetingTypeContainer")))

directory_URL = "https://pub-calgary.escribemeetings.com/?Year=2022"

driver.get(directory_URL)


past_meetings_container = driver.find_element(By.ID, "PastMeetingTypesAccordian")

past_meetings = past_meetings_container.find_elements(By.CLASS_NAME, "MeetingTypeList")

for past_meeting in past_meetings:
    if past_meeting.is_displayed():
        past_meeting.find_element(By.TAG_NAME, "a").click()

        wait.until(EC.url_contains("&Expanded="))

        # print(past_meeting.get_attribute("class"))
        # print(past_meeting.find_element(By.TAG_NAME, "div").get_attribute("class"))

        wait.until(lambda d: 'Loaded' in el.get_attribute('class'))
        # sleep(3)

        resource_container = past_meeting.find_element(By.TAG_NAME, "div").get_attribute("class")

        print(resource_container)

        # meeting_content = resource_container.find_element(By.TAG_NAME, "div")

        # for meeting in past_meeting.find_elements(By.TAG_NAME, "div"):
        #     print(meeting.text)
        #     print(meeting.get_attribute("href"))

        break



# Upload to database

driver.quit()