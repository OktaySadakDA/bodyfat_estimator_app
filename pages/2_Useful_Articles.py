import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import webbrowser


st.set_page_config(page_title='Useful Articles')
st.sidebar.success('Please select a page')

st.divider()

'#### Finding Your Body Density With A Skinfold Caliper'

button0 = st.button('(Click here to read) Body Density Equations: Durnin & Womersley.')
if button0:
  webbrowser.open('https://www.topendsports.com/testing/density-durnin-womersley.htm')

st.divider()

'#### Defining Adult Overweight & Obesity | Centers For Disease Control And Prevention'

button1 = st.button('(Click here to read) Overweight & Obesity.')
if button1:
  webbrowser.open('https://www.cdc.gov/obesity/basics/adult-defining.html')

st.divider()

'#### Calculate Your Body Mass Index'

button2 = st.button('(Click here to read) Calculate your BMI.')
if button2:
  webbrowser.open('https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm')

st.divider()


'#### Obesity Profile: short statistical commentary May 2023'

button3 = st.button('(Click here to read) Statistical commentary May 2023.')
if button3:
  webbrowser.open('https://www.gov.uk/government/statistics/obesity-profile-update-may-2023/obesity-profile-short-statistical-commentary-may-2023')

st.divider()

'#### What\'s the best way to measure body fat?'

button4 = st.button('(Click here to read) Article from British Heart Foundation.')
if button4:
  webbrowser.open('https://www.gov.uk/government/statistics/obesity-profile-update-may-2023/obesity-profile-short-statistical-commentary-may-2023')

st.divider()



