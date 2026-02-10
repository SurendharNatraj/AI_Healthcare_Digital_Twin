import streamlit as st
import pickle
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(".."))

from model.digital_twin import (
    calculate_health_score,
    health_status,
    health_tips
)



# Load trained model


st.set_page_config(page_title="AI Healthcare Digital Twin", layout="centered")

st.title("🩺 AI-Powered Preventive Healthcare Digital Twin")

st.write("Enter your daily health details below:")

# User Inputs
age = st.slider("Age", 18, 80, 30)
steps = st.slider("Daily Steps", 2000, 12000, 6000)
sleep = st.slider("Sleep Hours", 4.0, 9.0, 7.0)
stress = st.slider("Stress Level", 1, 10, 5)

# Create input dataframe
input_data = pd.DataFrame([[age, steps, sleep, stress]],
                          columns=["age", "steps", "sleep_hours", "stress_level"])

# Digital Twin Score
score = calculate_health_score(steps, sleep, stress)

st.subheader("🧠 Digital Twin Health Score")
st.metric("Health Score", score)

st.subheader("📊 Health Status")
st.success(health_status(score))

# AI Prediction
st.subheader("🤖 AI Risk Assessment")

status = health_status(score)

if status == "High Risk":
    st.error("High health risk detected")
elif status == "Medium Risk":
    st.warning("Moderate health risk detected")
else:
    st.success("Low health risk")

# Tips
st.subheader("💡 Personalized Health Tips")
tips = health_tips(steps, sleep, stress)

if tips:
    for tip in tips:
        st.write("•", tip)
else:
    st.write("You're doing great! Keep it up 👏")
