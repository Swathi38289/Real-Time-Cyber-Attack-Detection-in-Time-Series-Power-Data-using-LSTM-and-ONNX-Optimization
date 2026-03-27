import streamlit as st
import requests
import pandas as pd

st.title("Smart Grid Cybersecurity Dashboard")

# Sliders
voltage = st.slider("Voltage", 200, 260, 230)
current = st.slider("Current", 5, 20, 10)
frequency = st.slider("Frequency", 49, 51, 50)
phase_angle = st.slider("Phase Angle", -10, 10, 0)

# Session state for graph
if "history" not in st.session_state:
    st.session_state.history = []

# Button
if st.button("Check"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "voltage": voltage,
            "current": current,
            "frequency": frequency,
            "phase_angle": phase_angle
        }
    ).json()

    st.write(response)

    # Store voltage history
    st.session_state.history.append(voltage)

# Graph
if st.session_state.history:
    chart_data = pd.DataFrame(st.session_state.history, columns=["Voltage"])
    st.line_chart(chart_data)