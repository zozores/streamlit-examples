import streamlit as st
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx

session_id = f"**Sessão:** {get_script_run_ctx().session_id}"

st.write(session_id)
