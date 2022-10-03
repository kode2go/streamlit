import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

col1, col2, col3 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.metric(label="Temperature", value="70 °F", delta="1.2 °F")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

col3.bar_chart(chart_data)
