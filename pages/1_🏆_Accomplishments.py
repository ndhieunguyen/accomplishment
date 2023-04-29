import streamlit as st
import pandas as pd
import datetime

from utils import make_clickable, create_clickable_link

### Config
st.set_page_config(
    page_icon="🏆",
)

### SIDEBAR
st.sidebar.markdown("<h1 style='text-align: center;'>Tools</h1>", unsafe_allow_html=True)
name = (
    st.sidebar.text_input(
        "Name",
        "",
        help="The phrase contained in the name of the accomplishment",
    )
    .lower()
    .strip()
)
organizations = [
    "Tuyen Thanh Primary school",
    "Vo Duy Duong secondary school",
    "Kien Tuong High school",
    "FPT University",
    "Coursera",
    "Kaggle",
]
organization = st.sidebar.multiselect(
    "Organization",
    organizations,
    help="The organization that recognized the accomplishment",
)

from_date = st.sidebar.date_input(
    "From date",
    value=datetime.date(2002, 8, 25),
    min_value=datetime.date(2002, 8, 25),
    max_value=datetime.date.today(),
    help="The lower bound of date range",
)

to_date = st.sidebar.date_input(
    "To date",
    value=None,
    help="The upper bound of date range",
)

sorted_by = st.sidebar.multiselect(
    "Sorted by",
    ["Name", "Organization", "Date"],
    help="The columns by which the data frame is sorted",
)

filter_button = st.sidebar.button("OK")


### MAIN
st.markdown("<h1 style='text-align: center;'>Accomplishment</h1>", unsafe_allow_html=True)


@st.cache_data
def load_data():
    data_frame = pd.read_csv("accomplishment.csv", index_col=0).reset_index(drop=True)
    data_frame["Date"] = pd.to_datetime(data_frame["Date"], format="%B %Y").dt.date
    return data_frame


data = load_data()


if filter_button:
    # filter by name
    data = data[data["Name"].str.lower().str.contains(name)]

    # filter by organization
    if len(organization) > 0:
        data = data[data["Organization"].isin(organization)]

    # filter by date
    if len(data) > 0 and from_date and to_date:
        data = data[(from_date <= data["Date"]) & (data["Date"] <= to_date)]

    # sort by
    data = data.sort_values(by=sorted_by)

    # create clickable name
    if len(data) > 0:
        data["Name"] = data.apply(lambda x: create_clickable_link(x["Name"], x["Link"]), axis=1)
    data = data.drop(["Link"], axis=1)

    # display data frame
    st.write(data.to_html(escape=False), unsafe_allow_html=True)
else:
    data["Name"] = data.apply(lambda x: create_clickable_link(x["Name"], x["Link"]), axis=1)
    data = data.drop(["Link"], axis=1)
    st.write(data.to_html(escape=False), unsafe_allow_html=True)

st.download_button(
    label="Download accomplishments as CSV",
    data=data.to_csv().encode("utf-8"),
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
