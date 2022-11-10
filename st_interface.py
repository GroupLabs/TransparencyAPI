import streamlit as st
import pandas as pd
import numpy as np

from st_utils.get_data import get_all_data, get_meeting_by_id

st.title('Transparency API Interface')

# number = st.number_input('Insert a number', step=1, min_value=0, max_value=len(data)-1, help="Enter meeting id")
# st.write('The current number is ', number)

# data[number]

meeting_ID = st.text_input('Meeting ID:')
st.write('Selected ID: ', meeting_ID)

data = get_meeting_by_id(number)

data