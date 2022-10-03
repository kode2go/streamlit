"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

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
    

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
