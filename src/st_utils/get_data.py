import streamlit as st

from utils.db_connect import connectMongo

@st.experimental_singleton
def init_connection():
    return connectMongo()

client = connectMongo()

@st.experimental_memo(ttl=6000)
def get_all_data():
    db = client.Calgary
    data = db.escribe_meetings.find()
    data = list(data)

    return data

@st.experimental_memo(ttl=6000)
def get_meeting_by_id(meeting_id):
    db = client.Calgary
    data = db.escribe_meetings.find_one({"meeting_id": meeting_id})

    return data