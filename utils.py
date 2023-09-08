import base64
import streamlit as st

prefix = "https://github.com/ndhieunguyen/accomplishment/blob/main/images/"
postfix = "?raw=true"


# def make_clickable(link: str):
#     return f'<a target="_blank" href="{prefix+link}">{"View"}</a>'


def create_clickable_link(name: str, link: str):
    if not link.startswith("https"):
        link = prefix + link + postfix
    return f'<a target="_blank" href="{link}">{name}</a>'


def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = (
        f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    )
    st.markdown(pdf_display, unsafe_allow_html=True)
