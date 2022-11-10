from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

directory_URL = "https://pub-calgary.escribemeetings.com/?Year=2022"

driver.get(directory_URL)


past_meetings_container = driver.find_element(By.ID, "PastMeetingTypesAccordian")

past_meetings = past_meetings_container.find_elements(By.CLASS_NAME, "MeetingTypeList")

print(len(past_meetings))

for past_meeting in past_meetings:
    if past_meeting.is_displayed():
        past_meeting.find_element(By.TAG_NAME, "a").click()

        wait.until(EC.title_contains("&Expanded="))

        print(driver.current_url)

        sleep(1)


sleep(1)

# Upload to database

driver.quit()