import streamlit as st
import pandas as pd
import datetime

from utils import make_clickable, create_clickable_link

### Config
st.set_page_config(
    page_title="Accomplishment ndhieunguyen",
    page_icon="🏆",
)

### SIDEBAR
st.sidebar.markdown("<h1 style='text-align: center;'>Tools</h1>", unsafe_allow_html=True)
name = st.sidebar.text_input("Name", "", help="The phrase contained in the name of the accomplishment").lower().strip()
organizations = [
    "Tuyen Thanh Primary school",
    "Vo Duy Duong secondary school",
    "Kien Tuong High school",
    "FPT University",
    "Coursera",
]
organization = st.sidebar.multiselect(
    "Organization",
    organizations,
    help="The organization that recognized the accomplishment",
)

from_year = st.sidebar.date_input("From date", value=datetime.date(2002, 8, 25), help="The lower bound of date range")
to_year = st.sidebar.date_input("To date", help="The upper bound of date range")

sorted_by = st.sidebar.multiselect(
    "Sorted by",
    ["Name", "Organization", "Date"],
    help="The columns by which the data frame is sorted",
)

filter_button = st.sidebar.button("OK")


### MAIN
# st.header("Accomplishment")
st.markdown("<h1 style='text-align: center;'>Accomplishment</h1>", unsafe_allow_html=True)
st.text("Nguyen Doan Hieu Nguyen - ndhieunguyen")


@st.cache_data
def load_data():
    return pd.read_csv("accomplishment.csv", index_col=0).reset_index(drop=True)


data = load_data()
# data["View"] = data["View"].apply(make_clickable)
data["Name"] = data.apply(lambda x: create_clickable_link(x["Name"], x["Link"]), axis=1)
data = data.drop(["Link"], axis=1)


if filter_button:
    data = data[data["Name"].str.lower().str.contains(name)]
    if len(organization) > 0:
        for org in organization:
            data = data[data["Organization"].str.contains(org)]
    # st.dataframe(data=data, use_container_width=True)
    data = data.sort_values(by=sorted_by)
    data = data.to_html(escape=False)
    st.write(data, unsafe_allow_html=True)
else:
    # st.dataframe(data=data, use_container_width=True)
    data = data.to_html(escape=False)
    st.write(data, unsafe_allow_html=True)

st.download_button(
    label="Download accomplishments as CSV",
    # data=data.to_csv().encode("utf-8"),
    data=data,
    file_name="ndhieunguyen_accomplishment.csv",
    mime="text/csv",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
