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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png",
    ],
    "Linkedin": [
        "https://linkedin.com/in/ndhieunguyen",
        "https://cdn-icons-png.flaticon.com/512/174/174857.png",
    ],
    "Facebook": [
        "https://www.facebook.com/ndhieunguyen/",
        "https://cdn-icons-png.flaticon.com/512/124/124010.png",
    ],
    "Instagram": [
        "https://www.instagram.com/ndhieunguyen/",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/2048px-Instagram_icon.png",
    ],
    "Github": [
        "https://github.com/ndhieunguyen",
        "https://cdn-icons-png.flaticon.com/512/25/25231.png",
    ],
    "Hackerrank": [
        "https://www.hackerrank.com/ndhieunguyen",
        "https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/160_Hackerrank_logo_logos-512.png",
    ],
}

st.sidebar.markdown(
    """
    <img src="https://github.com/ndhieunguyen/accomplishment/blob/main/images/ndhieunguyen_nobackground.png?raw=true" style="margin-bottom: 0; padding-bottom: 0; height: auto; max-width: 100%;">
    <h1 style='text-align: center; margin-top: 0; margin-bottom: 0; padding-top: 0'>Hieu Nguyen</h1>
    <h2 style='text-align: center; margin-top: 0; margin-bottom: 0; padding-top: 0;'>Artifical Intelligence major student</h2>
    <hr style='text-align: center; margin-top: 0; margin-bottom: 0; padding-top: 0'>
    <h3 style='text-align: center;'>Contact</h3>
    """,
    unsafe_allow_html=True,
)

display_icons = ""
for page, link in profile_pages.items():
    display_icons += f'<a href="{link[0]}"> <img src="{link[1]}" width=30> </a>'


st.sidebar.markdown(
    '<div class="grid-container" style="text-align: center;">' + display_icons + "</div>",
    unsafe_allow_html=True,
)


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

st.header("Honors and Awards")
st.markdown(
    """
    - Achieved 100% scholarship at FPT University
    - Won third prize in FPT University Math Olympic 2022
    - Achieved FPT University Golden Toad of Engineering Major - Spring 2022
    - Won first prize at FPT Education Hackathon 2022
    - Finalist at FPT Education Resfes 2023
    """,
)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
