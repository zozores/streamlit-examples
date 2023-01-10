import streamlit as st
from datetime import datetime

st.title("Clock")
clock = st.empty()
while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info(f"**Current time:** {time}")
    if time == "23:15:50":
        clock.empty()
        st.warning("Alarm!!")
        break
