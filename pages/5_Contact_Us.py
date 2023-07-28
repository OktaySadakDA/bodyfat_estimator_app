import streamlit as st
from PIL import Image

st.set_page_config(page_title='Contact Details')
st.sidebar.success('Please select a page')

import webbrowser

'### Click \'Contact us!\' button to send us an e-mail.'

def open_support_ticket():
    email_link = "mailto:oktay.sadak@outlook.com"
    webbrowser.open(email_link)

st.button("Contact us!", on_click=open_support_ticket)
