# TransparencyAPI 

> Check out the requirements given by Pixeltree here: [Pixeltree Notion](https://pixeltree.notion.site/City-Council-Scraping-34a2f5a24d59400faf9a128f2653ebf2)

This project is part of a collaborative effort with Pixeltree Inc. to build a more transparent future. Our objective is to transform political activities into clear and compliant data that may be used to develop further insights.

---

*August 24, 2022*

The program will be given a url as an input. It should retuen a JSON output of all the contents of the HTML document. Take a look at an example input:
[example meeting minutes](https://pub-calgary.escribemeetings.com/Meeting.aspx?Id=9a27aea6-df27-4322-907f-164396fcf3b0&Agenda=PostMinutes&lang=English).
All the data we need is in this structured HTML. All we need to do is take out the information and return it in a JSON. **Implement with Python.**

Find more meeting minutes here: [meeting minutes dir](https://pub-calgary.escribemeetings.com/?Expanded=Audit%20Committee&Year=2022)

### What we want

- the UID of the meeting (found in the URL) (e.g. `9a27aea6-df27-4322-907f-164396fcf3b0`)
- who is present in the meeting
- who is present in roll call (check out the image below; these are the people that are able to vote)

![Untitled](https://pixeltree.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Feaa43fa3-4202-4d4e-a8c7-41aca3afb547%2FUntitled.png?table=block&id=de67cb23-656c-452d-816e-203ccfe11102&spaceId=42923d5a-a9d1-4f96-bd75-1d60d5709922&width=2000&userId=&cache=v2)

- list of all the motions
    - title of the motion
    - who it was moved by
    - other details
    - whether or not the motion was carried
    - links to any attachments (just the url)

### What we don't want

- information stored in the attachments
- information from the accompanying meeting video
- data processing

## Tasks

RETRIEVING:
- [ ] meeting UID
- [x] who is present in meeting
- [x] roll call
- [ ] motions
  - [ ] title
  - [ ] who it was moved by
  - [ ] other details
  - [ ] whether the motion was carried
  - [ ] attachment links

OTHER:
- [ ] transforming to JSON

BONUS:
- [ ] add into REST API

Use this repository to your heart's content. Just ensure that you don't overwrite other's work by building on your own branch. We will merge together on Friday! If you have any questions, otr get stuck on anything do not hesitate to reach out. Have fun! :smile:

## References
- [Beautiful Soup Simple Tutorial](https://realpython.com/beautiful-soup-web-scraper-python/)
- [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

