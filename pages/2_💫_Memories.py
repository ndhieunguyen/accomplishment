import streamlit as st

st.set_page_config(
    page_icon="💫",
)

st.title("To be continued...")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
