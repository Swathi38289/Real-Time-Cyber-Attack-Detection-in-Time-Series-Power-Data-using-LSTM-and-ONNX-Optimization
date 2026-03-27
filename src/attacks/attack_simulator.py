import pandas as pd
import numpy as np

def inject_attacks(df, attack_ratio=0.1):
    df = df.copy()
    n_attacks = int(len(df) * attack_ratio)

    attack_indices = np.random.choice(df.index, n_attacks, replace=False)

    for idx in attack_indices:
        df.loc[idx, "voltage"] *= np.random.uniform(1.2, 1.8)
        df.loc[idx, "current"] *= np.random.uniform(1.2, 1.5)
        df.loc[idx, "label"] = 1  # attack

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/pmu_data.csv")
    attacked_df = inject_attacks(df)

    attacked_df.to_csv("data/pmu_attacked.csv", index=False)
    print("Attack injected!")