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
st.sidebar.markdown(
    """
<div class="markdown-text-container stText" style="width: 698px;">
<footer>
<p></p>                    
</footer>
<div style="font-size: 12px;">
Hello World v0.1
</div>
<div style="font-size: 12px;">
Hello World LLC.
</div>
    """,
    unsafe_allow_html=True,
)
st.title("Hello World")
