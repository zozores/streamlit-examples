import streamlit as st
from PIL import Image

icon = Image.open("ch03/favicon.ico")
st.set_page_config(
    page_title="Hello World",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://streamlit.io",
        "Report a Bug": "https://github.com",
        "About": "About the application: **Hello World**",
    },
)
st.sidebar.title("Hello World")
st.title("Hello World")
