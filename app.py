import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Career Roadmap",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Career Roadmap App")

st.write(
    "Discover suitable AI & technology careers "
    "and get a personalized learning roadmap."
)

st.markdown("---")

# User information
st.header("👤 Student Information")

name = st.text_input("Enter your name")

# Skills
st.header("📊 Skill Assessment")

python_skill = st.slider("Python", 1, 10, 5)
ml_skill = st.slider("Machine Learning", 1, 10, 5)
sql_skill = st.slider("SQL", 1, 10, 5)
problem_solving = st.slider("Problem Solving", 1, 10, 5)
communication = st.slider("Communication", 1, 10, 5)

# Prediction button
if st.button("🎯 Predict My Career"):

    st.success("Career prediction module will be connected next!")

    st.write("### Your Skills")

    st.write("Python:", python_skill)
    st.write("Machine Learning:", ml_skill)
    st.write("SQL:", sql_skill)
    st.write("Problem Solving:", problem_solving)
    st.write("Communication:", communication)
