import streamlit as st

st.set_page_config(page_title="Education Platform", page_icon="📚", layout="centered")

st.title("📚 Education Platform")
st.write("Welcome to the Education Platform. Select a course below:")

courses = {
    "Railway science foundation": "https://t.me/+Ja5IJyCmnMVkM2Vl",
    "CGL +  CHSL + MTS MAINS": "https://t.me/+DumAzg8tD3I5NDc1",
    "Machine Learning Basics": "https://example.com/ml",
    "Web Development": "https://example.com/webdev"
}
st.image("home.jpg", caption="Welcome to the Education Platform", use_column_width=True)


for course, link in courses.items():
    st.markdown(f"[🔗 {course}]({link})")

st.write("### 📢 Connect with us on Social Media")
st.markdown("[📢 Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")
st.markdown("[ Follow us on Whatsapp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")
st.markdown("[📷 Follow us on Instagram](https://instagram.com/example)")
