import streamlit as st
import pandas as pd
import numpy as np

st.header ('Line chart')

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['viens','divi','tris'])

st.line_chart(chart_data)

#################################

st.header('st.selectbox')

option = st.selectbox(
  'Kāda ir Tava mīļākā krāsa?',
  ('Zaļa','Zila','Sarkana'))

#################################

st.header('st.multiselect')

options = st.multiselect(
  'Kādas ir Tavas mīļākās krāsas vairākas',
  ['Melna','Sarkana','Zaļa','Zila'],
  ['Dzeltena','Brūna'])

st.write('Tu izvēlējies:', options)