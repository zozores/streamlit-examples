import streamlit as st
import pandas as pd

st.title("Page 1")
st.session_state["page_state"] = "Page 1"
st.sidebar.write(f"**Page:** {st.session_state['page_state']}")

if "df" not in st.session_state:
    st.session_state["df"] = None
if "rows" not in st.session_state:
    st.session_state["rows"] = None

file = st.file_uploader("Upload File")
if file is not None:
    df = pd.read_csv(file)
    st.session_state["df"] = df
if st.session_state["df"] is not None:
    rows = st.slider(
        "Rows to display",
        value=st.session_state["rows"],
        min_value=1,
        max_value=len(st.session_state["df"]),
    )
    st.session_state["rows"] = rows
    st.write(st.session_state["df"].iloc[: st.session_state["rows"]])
