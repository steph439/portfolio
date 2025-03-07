import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Student Portfolio", page_icon="🎓")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact"])

# Home Section
if page == "Home":
    st.title("🎓 Student Portfolio")

    # Profile Image Upload
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="Uploaded Image")
    
    st.write(" hands-on experience in building projects and solving real-world problems.")

    # Student Details
    name = st.text_input("Name:", "DEUHIKBE BIANBAIB STEPHANE.")
    location = st.text_input("Location:", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study:", "Computer Science, SWE")
    university = st.text_input("University:", "INES - Ruhengeri")
    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🎓 {university}")

    # Resume Download
    try:
        with open("Stephane_CV_Phoenix.pdf", "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Stephane_CV_Phoenix.pdf", data=resume_bytes, file_name="Stephane_CV_Phoenix.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("❌ Resume file not found!")

    st.markdown("---")
    st.subheader("About Me")
    about_me = st.text_area("passionate about technology and software development")
    st.write(about_me)

# Projects Section
elif page == "Projects":
    st.title("💻 My Projects")

    with st.expander("📊 Malaria test"):
        st.write("Individual Project using Python")

    with st.expander("🤖 Malaria Diagnosis System"):
        st.write("Group Project using Python")


# Skills Section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)

    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)

    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    st.subheader("Certifications & Achievements")
    st.write("✔ Completed AI & ML in Business Certification")
    st.write("✔ Certified AI in Research and Course Preparation for Education")

# Settings Section
elif page == "Settings":
    st.title("🎨 Customize Your Profile")

    st.subheader("Upload a Profile Picture")
    uploaded_image = st.file_uploader("Choose a file", type=["jpg", "png"])
    if uploaded_image:
        st.image(uploaded_image, width=150)

    st.subheader("✍ Edit Personal Info")
    name = st.text_input("Your Name", "DEUHIKBE BIANBAIB STEPHANE.")
    location = st.text_input("Your Location", "Musanze, Rwanda")

# Contact Section
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully")

    st.write("📧 Email: ug2216592.ac.rw")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/stephane-deuhikbe-bianbaibe-03b39b355/)")
    st.write("[📂 GitHub](https://github.com/steph439)")

# Sidebar Footer
st.sidebar.write("---")
