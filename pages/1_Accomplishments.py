import streamlit as st
import pandas as pd
import datetime

from utils import create_clickable_link

### Config
st.set_page_config(
    page_icon="🏆",
)


### DATA
@st.cache_data
def load_data():
    data_frame = pd.read_csv("accomplishment.csv", index_col=0).reset_index(drop=True)
    data_frame["Date"] = pd.to_datetime(data_frame["Date"], format="%B %Y").dt.date
    data_frame.sort_values(by=["Date"])
    return data_frame


original_data = load_data()

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
organizations = sorted(list(set(original_data["Organization"])))
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

### MAIN
st.markdown("<h1 style='text-align: center;'>Accomplishment</h1>", unsafe_allow_html=True)


data = original_data.copy()

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
clickable_data = data.copy()
if len(clickable_data) > 0:
    clickable_data["Name"] = clickable_data.apply(lambda x: create_clickable_link(x["Name"], x["Link"]), axis=1)
clickable_data = clickable_data.drop(["Link"], axis=1)

# display data frame
st.write(clickable_data.to_html(escape=False), unsafe_allow_html=True)

_, col_center, _ = st.columns((2, 1, 2))
with col_center:
    st.download_button(
        label="Download data",
        data=data.to_csv().encode("utf-8"),
        file_name="ndhieunguyen_accomplishment.csv",
        mime="text/csv",
        use_container_width=True,
    )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
