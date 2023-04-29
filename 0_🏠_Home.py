import streamlit as st

### Config
st.set_page_config(
    page_title="Hieu Nguyen",
    page_icon="💻",
)


st.markdown(
    """
    <h1 style='text-align: center;'>Welcome to my home page</h1>
    """,
    unsafe_allow_html=True,
)

profile_pages = {
    "Gmail": [
        "mailto:hieunguyen.kientuong@gmail.com",
        "https://cdn-icons-png.flaticon.com/512/281/281769.png",
    ],
    "Github": [
        "https://github.com/ndhieunguyen",
        "https://cdn-icons-png.flaticon.com/512/25/25231.png",
    ],
    "Linkedin": [
        "https://linkedin.com/in/ndhieunguyen",
        "https://cdn-icons-png.flaticon.com/512/174/174857.png",
    ],
    "Hackerrank": [
        "https://www.hackerrank.com/ndhieunguyen",
        "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/160_Hackerrank_logo_logos-512.png",
    ],
    "Facebook": [
        "https://www.facebook.com/ndhieunguyen/",
        "https://cdn-icons-png.flaticon.com/512/124/124010.png",
    ],
}

st.sidebar.markdown(
    f'<img src="https://github.com/ndhieunguyen/accomplishment/blob/main/images/ndhieunguyen_nobackground.png" style="margin-bottom: 0; padding-bottom: 0;">',
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """
    <h1 style='text-align: center; margin-top: 0; margin-bottom: 0; padding-top: 0'>Hieu Nguyen</h1>
    <h2 style='text-align: center; margin-top: 0; margin-bottom: 0; padding-top: 0;'>AI major student</h2>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.sidebar.columns([0.2, 1])
for page, link in profile_pages.items():
    with col1:
        st.image(link[1], width=25)
    with col2:
        st.markdown(f"[{page}]({link[0]})")

st.header("Short Bio")
st.markdown(
    """
    I am a final-year student at [FPT University](https://hcmuni.fpt.edu.vn/), specializing in Artificial Intelligence, 
    who has excelled academically and earned a full scholarship for studies.\n 
    I started my academic journey at Tuyen Thanh Primary school, followed by [Vo Duy 
    Duong Secondary school](https://www.facebook.com/THCSVODUYDUONG), and eventually graduating from [Kien Tuong High School](https://www.facebook.com/KTHSchool). 
    Currently, I am working as an AI intern at [Gradients Technologies](https://www.linkedin.com/company/gradients-tech/), where i am 
    actively involved in research on computer vision and natural language processing. 
    \n With my passion for AI and dedication to learning, i want to make a 
    significant impact in the field of technology, especially Artificial Intelligence.
    """,
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
