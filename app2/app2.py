"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    #read csv
    df1=pd.read_csv(uploaded_file)
    st.write(df1)
else:
    st.warning('you need to upload a file')
    
