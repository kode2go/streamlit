"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame(
    {
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }
)
st.write(df)

uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    #read csv
    df1=pd.read_csv(uploaded_file)
    st.write(df1)
else:
    st.warning('you need to upload a file')
    
import numpy as np

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
