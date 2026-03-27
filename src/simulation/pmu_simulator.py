import numpy as np
import pandas as pd

def generate_pmu_data(n_samples=1000):
    np.random.seed(42)

    time = np.arange(n_samples)

    voltage = 230 + np.random.normal(0, 2, n_samples)
    current = 10 + np.random.normal(0, 0.5, n_samples)
    frequency = 50 + np.random.normal(0, 0.02, n_samples)
    phase_angle = np.random.normal(0, 1, n_samples)

    df = pd.DataFrame({
        "time": time,
        "voltage": voltage,
        "current": current,
        "frequency": frequency,
        "phase_angle": phase_angle,
        "label": 0  # normal
    })

    return df

if __name__ == "__main__":
    df = generate_pmu_data(1000)
    df.to_csv("data/pmu_data.csv", index=False)
    print("PMU data generated!")