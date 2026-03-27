import joblib
import numpy as np
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Load model
model = joblib.load("models/model.pkl")

# Define input type
initial_type = [("float_input", FloatTensorType([None, 4]))]

# Convert to ONNX
onnx_model = convert_sklearn(model, initial_types=initial_type)

# Save
with open("models/model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("ONNX model saved!")