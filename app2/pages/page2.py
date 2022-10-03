import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

col1.st.line_chart(chart_data)
col2.st.line_chart(chart_data)
col3.st.line_chart(chart_data)
