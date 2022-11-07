from web_scraper_summarizer import minutes_scraper
from utils.utils import isValidURL

import json
import sys
import os

# Web scraping CLI

# Debug mode
DEBUG = False

# URL to scrape
URL = str(sys.argv[1])

while not isValidURL(URL):
    print("Invalid or missing URL input")
    print("Please enter a URL now:")

    URL = input()

# Get output directory
out_dir = ""
if len(sys.argv) == 3:
    out_dir = sys.argv[2]
else:
    out_dir = os.getcwd()

###

JSON_obj = minutes_scraper(URL)

# Serialize and write to "meeting_minutes.json"
with open(f"{out_dir}/meeting_minutes.json", "w") as out:
    json.dump(JSON_obj, out, indent=4)