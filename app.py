import streamlit as st
import json

from resume_parser import extract_text_from_pdf, extract_skills
from skill_matcher import match_skills
from roadmap_generator import generate_roadmap

#  PAGE CONFIG (ONLY ONCE & MUST BE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="SkillGap Pro", page_icon="📊", layout="wide")

#  CUSTOM CSS
st.markdown("""
<style>
.block-container {padding-top: 2rem;}
h1, h2, h3 {font-weight: 600;}

[data-testid="stMetric"] {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
}

.stButton>button {
    background-color: #6366F1;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

#  SIDEBAR
with st.sidebar:
    st.title("SkillGap Pro 🚀")
    menu = st.radio("", ["📄 Upload Resume", "📊 Dashboard", "📘 Learning Roadmap"])

#  HERO SECTION
st.title("📊 SkillGap Pro")
st.write("Bridge your skill gap & get placement ready.")

#  FILE UPLOAD
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

#  ROLE SELECTION
role = st.selectbox(
    "Select Job Role",
    ["Data Scientist", "Backend Developer", "AI Engineer"]
)

#  MAIN LOGIC
if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)
    user_skills = extract_skills(text)

    with open("data/roles.json") as f:
        roles = json.load(f)

    score, matched, missing = match_skills(user_skills, roles[role])
    roadmap = generate_roadmap(missing)

    #  METRICS
    col1, col2, col3 = st.columns(3)
    col1.metric("Match Score", f"{score:.0f}%")
    col2.metric("Skills Found", len(user_skills))
    col3.metric("Skills Missing", len(missing))

    st.progress(int(score))

    #  TWO COLUMN LAYOUT
    left, right = st.columns(2)

    with left:
        st.subheader("✅ Your Skills")
        st.write(" ".join([f"`{skill}`" for skill in user_skills]))

    with right:
        st.subheader("❌ Missing Skills")
        st.write(" ".join([f"`{skill}`" for skill in missing]))

    #  PLACEMENT READINESS
    st.subheader("Placement Readiness")
    if score >= 75:
        st.success("You are READY for placements 🚀")
    elif score >= 50:
        st.warning("You are halfway there — keep learning 📚")
    else:
        st.error("You need more skills 😅")

    #  ROADMAP
    st.subheader("Your Learning Plan")
    for step in roadmap:
        st.checkbox(step)

    #  DOWNLOAD BUTTON
    roadmap_text = "\n".join(roadmap)
    st.download_button("Download Roadmap", roadmap_text, file_name="roadmap.txt")

#  FOOTER
st.markdown("---")
st.caption("Built with ❤️ by Nikhil")