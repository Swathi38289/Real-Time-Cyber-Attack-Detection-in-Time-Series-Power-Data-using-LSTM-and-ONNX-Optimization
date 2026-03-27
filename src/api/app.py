
from fastapi import FastAPI
import numpy as np
from tensorflow.keras.models import load_model

app = FastAPI()

model = load_model("models/lstm_model.h5")

sequence_buffer = []
TIME_STEPS = 10

@app.get("/")
def home():
    return {"message": "Smart Grid Cybersecurity API Running (LSTM)"}

@app.post("/predict")
def predict(voltage: float, current: float, frequency: float, phase_angle: float):

    global sequence_buffer

    sequence_buffer.append([voltage, current, frequency, phase_angle])

    if len(sequence_buffer) > TIME_STEPS:
        sequence_buffer.pop(0)

    if len(sequence_buffer) < TIME_STEPS:
        return {"message": "Collecting data...", "status": "WAIT"}

    input_data = np.array([sequence_buffer])

    prediction = model.predict(input_data)[0][0]
    label = 1 if prediction > 0.5 else 0

    return {
        "prediction": label,
        "status": "ATTACK" if label == 1 else "NORMAL"
    }