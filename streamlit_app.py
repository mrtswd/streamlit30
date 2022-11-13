import streamlit as st
import pandas as pd
import numpy as np

st.header ('Line chart')

chart data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['viens','divi','tris'])

st.line_chart(chart_data)
