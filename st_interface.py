import streamlit as st
import pandas as pd
import numpy as np

from src.st_utils.get_data import get_all_data, get_meeting_by_id

st.title('Transparency API Interface')

meeting_ID = st.text_input('Meeting ID:')
st.write('Selected ID: ', meeting_ID)

data = get_meeting_by_id(meeting_id=meeting_ID)

data