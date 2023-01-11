import streamlit as st
from pages.subpages.subpage_1_1 import run_subpage_1_1
from pages.subpages.subpage_1_2 import run_subpage_1_2

st.markdown("# Page 1")
st.sidebar.markdown("# Page 1")

subpages_page_1 = {"Subpage 1.1": run_subpage_1_1, "Subpage 1.2": run_subpage_1_2}

st.sidebar.subheader("Subpage selection")
subpage_selection = st.sidebar.selectbox(
    "Please select a subpage", tuple(subpages_page_1.keys())
)
subpages_page_1[subpage_selection]()
