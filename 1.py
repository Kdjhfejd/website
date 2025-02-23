import streamlit as st

# Set page configuration
st.set_page_config(page_title="Education Platform", page_icon="📚", layout="wide")

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.sidebar.button("🌙 Toggle Dark Mode", on_click=toggle_dark_mode)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Courses", "Feedback & Suggestions"])

def home_page():
    st.title("📚 Education Platform")
    st.image("home.jpg", caption="Welcome to the Education Platform", use_column_width=True)
    st.write("Explore our wide range of courses and connect with us on social media.")
    
    # Social Media Links
    st.write("### 📢 Connect with us on Social Media")
    st.markdown("[📢 Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")
    st.markdown("[💬 Follow us on WhatsApp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")
    st.markdown("[📷 Follow us on Instagram](https://www.instagram.com/mkraajltp?igsh=MXRvMHZ3Zzg4ZHhwbw%3D%3D)")

def courses_page():
    st.title("🎓 Explore Our Courses")
    
    # Search Bar for Courses
    search_query = st.text_input("🔍 Search for a course:", "")
    
    # Course Categories
    categories = ["All", "Competitive Exams", "Development", "Medical", "Entertainment", "Hacking"]
    selected_category = st.selectbox("📂 Select Category", categories)
    
    courses = {
        "MAIN CHENNAL": ("https://t.me/+XuIEiecTujMxODNl", "General"),
        "SSC BANKING RAILWAY": ("https://t.me/+6rX0Xxg3FtBmYTE1", "Competitive Exams"),
        "UPSC": ("https://t.me/+vBpYFICH6HczY2M9", "Competitive Exams"),
        "INFINITE COURSES": ("https://t.me/+PTnRqzn8PfczM2I1", "Development"),
        "NEW COURSES 2025": ("https://t.me/+FMHvMLefobowZjRl", "Development"),
        "SKILL DEVELOPMENT": ("https://t.me/+T_XBkV5xs3g3MjZl", "Development"),
        "MEDICAL COURSES": ("https://t.me/+60rJJcg7bcFlODRl", "Medical"),
        "ENTERTAINMENT": ("https://t.me/+-2ca3mBA87w5YTll", "Entertainment"),
        "HACKING RESOURCES": ("https://t.me/+6QVRmkwFDrRiOGNl", "Hacking"),
    }
    
    # Filter Courses
    filtered_courses = {name: link for name, (link, cat) in courses.items() if 
                        (search_query.lower() in name.lower()) and (selected_category == "All" or cat == selected_category)}
    
    if filtered_courses:
        for course, link in filtered_courses.items():
            st.markdown(f"- [{course}]({link}) ⭐⭐⭐⭐☆")
    else:
        st.write("❌ No courses found. Try a different keyword.")
    
    # Allow users to send a course
    st.write("### ➕ Add a New Course")
    course_name = st.text_input("Course Name")
    course_link = st.text_input("Course Link")
    if st.button("Submit Course"):
        if course_name and course_link:
            with open("courses.txt", "a") as f:
                f.write(f"{course_name}: {course_link}\n")
            st.success("✅ Course submitted successfully!")
        else:
            st.warning("⚠️ Please fill both fields.")

def feedback_page():
    st.title("💬 Feedback & Suggestions")
    
    # Feedback Form
    st.write("We appreciate your feedback! Please let us know your thoughts before you leave.")
    feedback = st.text_area("📝 Your Feedback")
    if st.button("Submit Feedback"):
        with open("feedback.txt", "a") as f:
            f.write(f"Feedback: {feedback}\n")
        st.success("✅ Thank you for your feedback! It has been saved.")
    
    # Suggestion Box
    st.write("### ✨ Have a Suggestion?")
    suggestion = st.text_area("💡 Drop your suggestions here!")
    if st.button("Send Suggestion"):
        with open("feedback.txt", "a") as f:
            f.write(f"Suggestion: {suggestion}\n")
        st.success("🚀 Suggestion sent successfully! It has been saved.")

# Display selected page
if page == "Home":
    home_page()
elif page == "Courses":
    courses_page()
elif page == "Feedback & Suggestions":
    feedback_page()
