import streamlit as st
import pandas as pd
import numpy as np

import json

from src.st_utils.get_data import *

st.title('Transparency API Interface')

# Using object notation
search_selectbox = st.sidebar.selectbox(
    "How would you like to search?",
    ("Meeting ID", "Date", "Meeting Type")
)

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

if search_selectbox == "Meeting ID":
    meeting_id = st.text_input('Meeting ID:')
    if meeting_id:
        st.write('Selected ID: ', meeting_id)
        data = get_meeting_by_id(meeting_id)
        st.write(data)

if search_selectbox == "Date":
    time_radio = st.radio(
        "Time included?",
        ("Yes", "No")
    )

    if time_radio == "Yes":
        date = st.date_input('Date:').strftime("%A, %B %d, %Y")
        time = st.time_input('Time:').strftime("%-I:%M %p")[:-1] + ".m."

        date_time = f"{date} at {time}"

        if date_time:
            st.write('Selected Date: ', date_time)
            data = get_meeting_by_datetime(date_time)
            if data:
                num = st.number_input("Meeting Number", step=1, max_value=len(data)-1, min_value=0)
                # st.download_button("download", json.dumps(data[num], indent=2).encode('utf-8'))
                st.write(data[num])

    elif time_radio == "No":
        date = st.date_input('Date:').strftime("%A, %B %d, %Y")
        if date:
            st.write('Selected Date: ', date)
            data = get_meeting_by_date(date)
            if data:
                num = st.number_input("Meeting Number", step=1, max_value=len(data)-1, min_value=0)
                # st.download_button("download", json.dumps(data[num], indent=2).encode('utf-8'))
                st.write(data[num])

if search_selectbox == "Meeting Type":
    meeting_type = st.text_input('Meeting Type:')
    if meeting_type:
        st.write('Selected Type: ', meeting_type)
        data = get_meeting_by_type(meeting_type)   
        if data:     
            num = st.number_input("Meeting Number", step=1, max_value=len(data)-1, min_value=0)
            # st.download_button("download", json.dumps(data[num], indent=2).encode('utf-8'))
            st.write(data[num])