import streamlit as st

hide_footer_style = """
<style>
.reportview-container .main footer {visibility: hidden;}
</style>
"""
st.markdown(hide_footer_style, unsafe_allow_html=True)

hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.title("Hello World")
st.title("Hello World")
