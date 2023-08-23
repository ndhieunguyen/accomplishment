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
    I started my academic journey at Tuyen Thanh Primary School, followed by [Vo Duy 
    Duong Secondary School](https://www.facebook.com/THCSVODUYDUONG), and eventually graduated from [Kien Tuong High School](https://www.facebook.com/KTHSchool). I used to work as an AI intern at [Gradients Technologies](https://www.linkedin.com/company/gradients-tech/), where I was 
    actively involved in research on computer vision and natural language processing. 
    \n With my passion for AI and dedication to learning, I want to make a significant impact in the technology field, especially Artificial Intelligence.
    """,
)

st.header("Honors and Awards")
st.markdown(
    """
    - 100% Scholarship at FPT University HCM [🔗](https://daihoc.fpt.edu.vn/trong-ky-thi-hoc-bong-khong-vi-than-nao-mang-lai-ky-tich-ngoai-ban-than-minh/)
    - Third prize of Algebra group in FPT Mathematics Olympic 2022 [🔗](https://www.facebook.com/fptaround/photos/a.403105523145779/4964859586970327/)
    - FPT University Golden Toad of Engineering Major Spring 2022 - the award for the most excellent student in a semester [🔗](https://www.facebook.com/fptaround/photos/a.5010487722407513/5010474842408801)
    - First prize at FPT Edu Hackathon 2022 - the competition on Algorithm and Blockchain application [🔗](https://fpt.edu.vn/tin-tuc/fpt-edu-tin-tuc-chung/quan-quan-bang-a-fpt-edu-hackathon-2022-vo-oa-cam-xuc-trong-giay-phut-len-ngoi)
    - Second prize at FPT University HCM Research Festival 2023 - the competition on Scientific Research at FPT University HCM
    - First prize at FPT Education Research Festival 2023 - the competition on Scientific Research at FPT Education [🔗](https://fpt.edu.vn/tin-tuc/fpt-edu-tin-tuc-chung/du-an-to-mau-cho-phim-don-sac-gianh-ngoi-quan-quan-tieu-ban-cntt-tai-fpt-edu-resfes-2023)
    """,
)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
