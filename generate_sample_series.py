import numpy as np
import pandas as pd

def generate_series(n=500, start_price=100.0, vol=0.01, anomaly_prob=0.02):
    rng = np.random.default_rng(42)
    returns = rng.normal(0, vol, n)
    prices = start_price * np.exp(np.cumsum(returns))
    volumes = rng.integers(1000, 20000, n)
    anomalies = rng.random(n) < anomaly_prob
    prices[anomalies] *= rng.uniform(0.8, 1.2, anomalies.sum())
    volumes[anomalies] *= rng.integers(2, 8, anomalies.sum())
    df = pd.DataFrame({
        "step": np.arange(n),
        "price": prices,
        "volume": volumes,
        "anomaly": anomalies
    })
    return df

if __name__ == "__main__":
    df = generate_series(500)
    import os
    os.makedirs("demo", exist_ok=True)
    df.to_csv("demo/demo_series.csv", index=False)
    print(df.head(10))
