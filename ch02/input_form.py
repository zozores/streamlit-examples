import streamlit as st

with st.form("feedback_form"):
    st.header("Feedback Form")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name:")
        rating = st.slider("Rating:", 0, 10, 5)
    with col2:
        dob = st.date_input("Date of Birth:")
        recommend = st.radio("Would you recommend?", ("Yes", "No"))

    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write(
        f"**Name:** {name} | **Date of Birth:** {dob} | **Rating:** {rating} | **Recommend:** {recommend}"
    )
