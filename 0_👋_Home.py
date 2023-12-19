import streamlit as st
import base64

name = "Sofia Ntalla"
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title=f"{name}'s Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write(f"**Author:** {name}")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is {name}</h1></div>""", unsafe_allow_html=True)


# ----- Profile image file -----
profile_image_file_path = "profile.jpeg"       

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt=f"{name}" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Student at EAE Business School"
course = "Big Data & Analytics"

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)
st.write(f"""<div style="text-align: center;"><h6><i>{course}</i></h6></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# 
st.write("""
- 🧑‍💻 Currently a student

- 🛩️ Previously: Technologist at Tata Steel

- 🏂 Writing at Greek feminist blog, swimming

- 📫 How to reach me: sophia.ntalla@gmail.com

- 🏠 Barcelona
        
- 💼 LinkedIn: www.linkedin.com/in/sofia-ntalla       
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
