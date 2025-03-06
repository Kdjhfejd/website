import streamlit as st

# Set page configuration
st.set_page_config(page_title="Education Platform", page_icon="📚", layout="wide")

# Dark Mode Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.markdown("<div style='text-align: center;'><button onclick='window.location.reload()' style='font-size:20px; padding:10px 20px; border-radius:10px;'>🌙 Toggle Dark Mode</button></div>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
st.sidebar.write("<----------------------------- Click the arrow to shuffle to other pages", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["Courses", "Home", "Feedback & Suggestions"])

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
        "VIP MEMBERS GROUP": ("https://t.me/+qM06_7HP4PdkNzk1", "GROWTH 💹"),
        "FREE UDEMY COURSES": ("https://t.me/+MEBmwvJ2XGUyYjA1", "INTERNATIONAL"),
        "MEDICAL COURSES": ("https://t.me/+60rJJcg7bcFlODRl", "Medical"),
        "ENTERTAINMENT": ("https://t.me/+-2ca3mBA87w5YTll", "Entertainment"),
        "PLACEMENT COURSES": ("https://t.me/+WVYzQmXTkWZkMDk1", "STUDY"),
        "HACKING RESOURCES": ("https://t.me/+6QVRmkwFDrRiOGNl", "Hacking")
    }
    
    # Filter Courses
    filtered_courses = {name: link for name, (link, cat) in courses.items() if 
                        (search_query.lower() in name.lower()) and (selected_category == "All" or cat == selected_category)}
    
    if filtered_courses:
        for course, link in filtered_courses.items():
            st.markdown(f"- [{course}]({link}) ⭐⭐⭐⭐☆")
    else:
        st.write("❌ No courses found. Try a different keyword.")
    
    # Google Form for Adding a New Course
    st.write("### ➕ Add a New Course")
    st.markdown("[📌 Submit a Course Here](https://forms.gle/CZtyg1CeXA39DTcW9) 🔗 (opens in a new tab)", unsafe_allow_html=True)

def home_page():
    st.title("📚 Education Platform")
    st.image("home.jpg", caption="Welcome to the Education Platform", use_column_width=True)
    st.write("Explore our wide range of courses and connect with us on social media.")
    
    # Social Media Links
    st.write("### 📢 Connect with us on Social Media")
    st.markdown("[📢 Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")
    st.markdown("[💬 Follow us on WhatsApp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")
    st.markdown("[📷 Follow us on Instagram](https://www.instagram.com/mkraajltp?igsh=MXRvMHZ3Zzg4ZHhwbw%3D%3D)")

def feedback_page():
    st.title("💬 Feedback & Suggestions")
    
    # Google Form for Feedback
    st.write("We appreciate your feedback! Please share your thoughts below.")
    st.markdown("[📝 Submit Feedback Here](https://forms.gle/CZtyg1CeXA39DTcW9) 🔗 (opens in a new tab)", unsafe_allow_html=True)

# Display selected page
if page == "Courses":
    courses_page()
elif page == "Home":
    home_page()
elif page == "Feedback & Suggestions":
    feedback_page()
