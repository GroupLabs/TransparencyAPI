from flask import Flask, request, jsonify
from web_scraper import minutes_scraper

import json

app = Flask(__name__)

@app.route("/scrape/")
def scrape():
    URL = json.loads(request.data.decode("utf-8"))["URL"]

    data = minutes_scraper(URL)

    if data == "Invalid URL":
        return data

    data["summary"] = summarize(data)

    return data


def summarize(data):

    # Use summarizer here

    return "summarized data"

app.run()