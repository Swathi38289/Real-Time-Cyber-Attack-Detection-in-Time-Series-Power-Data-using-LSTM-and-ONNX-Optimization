import joblib
import time
import numpy as np

model = joblib.load("models/model.pkl")

sample = np.array([[230, 10, 50, 0]])

# Normal inference
start = time.time()
for _ in range(1000):
    model.predict(sample)
end = time.time()

print("Normal Model Time:", end - start)

# Simulated optimized (just demo)
start = time.time()
for _ in range(1000):
    model.predict(sample)
end = time.time()

print("Optimized Model Time (Simulated):", end - start)