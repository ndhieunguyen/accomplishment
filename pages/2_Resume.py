import streamlit as st
import os
from utils import show_pdf

st.set_page_config(
    page_icon="📄",
)

file_path = os.path.abspath(os.path.join("images", "Nguyen_Doan_Hieu_Nguyen__Resume.pdf"))
show_pdf(file_path)

with open(file_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# st.sidebar.download_button(
#     label="Download Resume",
#     data=PDFbyte,
#     file_name="Nguyen_Doan_Hieu_Nguyen__Resume.pdf",
#     mime="application/octet-stream",
# )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
