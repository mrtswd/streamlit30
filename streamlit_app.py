import streamlit as st
import pandas as pd
import numpy as np
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')

age=st.slider('How old are you?', 0, 130, 25)
st.write('I am', age, 'years old')

st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0,75.0))

st.write('Values:', values)

st.subheader('Range time slider')

appointment=st.slider(
    'Schedule your appointment:',
    value=(time(11,30), time(14,45))
)

st.write('You are scheduled for:', appointment)

st.subheader('Datetime slider')

start_time=st.slider(
    "When do you start?",
    value=datetime(2022,1,1,9,30),
    format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)

#################################

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
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

#################################

st.header('st.checkbox')
st.write ('Ko Jūs gribētu pasūtīt?')
saldejums = st.checkbox('Saldējums')
kafija = st.checkbox('Kafija')
cola = st.checkbox('Cola')

if saldejums:
  st.write("Lieliski, te būs 🍦")

if kafija:
  st.write("Jūsu gardā ☕ jau klāt!")

if cola:
  st.write("Saņemiet 🥤")