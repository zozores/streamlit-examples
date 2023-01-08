import streamlit as st

col1, col2 = st.columns(2)

with col1:
    number_1 = st.number_input("Number 1", value=0, step=1)
with col2:
    number_2 = st.number_input("Number 2", value=0, step=1)

st.info(f"**{number_1}/{number_2}=** {number_1/number_2}")
