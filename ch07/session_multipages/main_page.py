import streamlit as st

if "page_state" not in st.session_state:
    st.session_state["page_state"] = None

st.title("Main Page")
st.session_state["page_state"] = "Main Page"
st.sidebar.write(f"**Page:** {st.session_state['page_state']}")
