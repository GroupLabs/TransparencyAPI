import streamlit as st
import pandas as pd
import numpy as np

from utils.db_connect import connectMongo

st.title('Transparency API Interface')

@st.experimental_singleton
def init_connection():
    return connectMongo()

client = connectMongo()


# @st.experimental_memo(ttl=6000)
# def get_all_data():
#     db = client.Calgary
#     data = db.escribe_meetings.find()
#     data = list(data)

#     return data

# data = get_all_data()

# number = st.number_input('Insert a number', step=1, min_value=0, max_value=len(data)-1, help="Enter meeting id")
# st.write('The current number is ', number)

# data[number]

number = st.text_input('Meeting ID:')
st.write('Selected ID: ', number)

@st.experimental_memo(ttl=6000)
def get_meeting_by_id(meeting_id):
    db = client.Calgary
    data = db.escribe_meetings.find_one({"meeting_id": meeting_id})

    return data

data = get_meeting_by_id(number)

data