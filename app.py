import streamlit as st

from career_predictor import predict_career
from roadmap import get_roadmap


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Career Roadmap",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Career Roadmap App")

st.write(
    "Discover a suitable career based on your skills "
    "and get a personalized learning roadmap."
)

st.markdown("---")


# -----------------------------
# Student Information
# -----------------------------
st.header("👤 Student Information")

name = st.text_input("Enter your name")


# -----------------------------
# Skill Assessment
# -----------------------------
st.header("📊 Skill Assessment")

python_skill = st.slider("🐍 Python", 1, 10, 5)
ml_skill = st.slider("🧠 Machine Learning", 1, 10, 5)
sql_skill = st.slider("🗄️ SQL", 1, 10, 5)
problem_solving = st.slider("🧩 Problem Solving", 1, 10, 5)
communication = st.slider("💬 Communication", 1, 10, 5)


# -----------------------------
# Career Prediction
# -----------------------------
if st.button("🎯 Predict My Career"):

    if not name:
        st.warning("Please enter your name first.")

    else:

        career, scores = predict_career(
            python_skill,
            ml_skill,
            sql_skill,
            problem_solving,
            communication
        )

        st.success(f"Hello {name}! Your recommended career is:")

        st.subheader(f"🎯 {career}")


        # -----------------------------
        # Career Scores
        # -----------------------------
        st.header("📊 Career Scores")

        for career_name, score in scores.items():
            st.write(
                f"**{career_name}:** {score:.2f} / 10"
            )


        # -----------------------------
        # Learning Roadmap
        # -----------------------------
        st.header("🗺️ Your Learning Roadmap")

        roadmap = get_roadmap(career)

        for step, topic in enumerate(roadmap, start=1):
            st.write(f"### Step {step}")
            st.info(topic)


        st.success(
            "🎉 Your personalized career roadmap has been generated!"
        )
