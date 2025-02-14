import streamlit as st

st.set_page_config(page_title="Education Platform", page_icon="📚", layout="centered")

st.title("📚 Education Platform")
st.write("Welcome to the Education Platform. Select a course below:")

courses = {
    "MAIN CHENNAL": "https://t.me/+XuIEiecTujMxODNl",
    "SSC BANKING RAILWAY ": "https://t.me/+6rX0Xxg3FtBmYTE1",
    "UPSC": "https://t.me/+vBpYFICH6HczY2M9",
    "VIP MEMBERS ": "https://t.me/+qM06_7HP4PdkNzk1",
    "INFINITE COURSES": "https://t.me/+PTnRqzn8PfczM2I1",
    "NEW COURSES 2025": "https://t.me/+FMHvMLefobowZjRl",
    "ENTERTAINMENT ": "https://t.me/+-2ca3mBA87w5YTll"

}
st.image("home.jpg", caption="Welcome to the Education Platform", use_column_width=True)


for course, link in courses.items():
    st.markdown(f"[🔗 {course}]({link})")

st.write("### 📢 Connect with us on Social Media")
st.markdown("[📢 Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")
st.markdown("[ Follow us on Whatsapp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")
st.markdown
