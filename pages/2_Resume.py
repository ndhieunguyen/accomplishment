import streamlit as st
import base64
from utils import show_pdf

file_path = "https://github.com/ndhieunguyen/accomplishment/blob/main/images/Nguyen_Doan_Hieu_Nguyen___AI_engineer___Resume.pdf"
show_pdf(file_path)

with open(file_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="Download Resume",
    data=PDFbyte,
    file_name="Nguyen_Doan_Hieu_Nguyen___AI_engineer___Resume.pdf",
    mime="application/octet-stream",
)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
