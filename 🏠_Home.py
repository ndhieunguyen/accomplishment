import streamlit as st

st.markdown(
    """
    <h1 style='text-align: center;'>Welcome to my home page</h1>
    """,
    unsafe_allow_html=True,
)

profile_pages = {
    "Github": "https://github.com/ndhieunguyen",
    "Linkedin": "https://linkedin.com/in/ndhieunguyen",
    "Hackerrank": "https://www.hackerrank.com/ndhieunguyen",
    "Facebook": "https://www.facebook.com/ndhieunguyen/",
}

columns = st.columns(len(profile_pages))
for i, col in enumerate(columns):
    col.markdown(
        f"""
        <a href="{list(profile_pages.values())[i]}">{list(profile_pages.keys())[i]}</a>
        """,
        unsafe_allow_html=True,
    )


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
