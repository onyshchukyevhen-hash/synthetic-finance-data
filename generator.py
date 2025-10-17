import argparse, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_series(n=500, start_price=100.0, vol=0.01, anomaly_prob=0.02):
    rng = np.random.default_rng(42)
    returns = rng.normal(0, vol, n)
    prices = start_price * np.exp(np.cumsum(returns))
    volumes = rng.integers(1000, 20000, n)
    anomalies = rng.random(n) < anomaly_prob
    prices[anomalies] *= rng.uniform(0.8, 1.2, anomalies.sum())
    volumes[anomalies] *= rng.integers(2, 8, anomalies.sum())
    return pd.DataFrame({"step": np.arange(n), "price": prices, "volume": volumes, "anomaly": anomalies})

def plot_series(df, stem):
    # price + anomalies
    ax = df["price"].plot()
    ax.set_title("Synthetic Price"); ax.set_xlabel("step"); ax.set_ylabel("price")
    an_idx = df.index[df["anomaly"]]
    ax.plot(an_idx, df.loc[an_idx, "price"], "o", markersize=4)
    plt.tight_layout(); plt.savefig(f"{stem}_price.png"); plt.close()

    # volume
    df["volume"].plot()
    plt.title("Synthetic Volume"); plt.xlabel("step"); plt.ylabel("volume")
    plt.tight_layout(); plt.savefig(f"{stem}_volume.png"); plt.close()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, default=500)
    p.add_argument("--vol", type=float, default=0.01)
    p.add_argument("--anomalies", type=float, default=0.02)
    args = p.parse_args()

    os.makedirs("demo", exist_ok=True)
    df = generate_series(args.days, 100.0, args.vol, args.anomalies)
    stem = f"demo/synthetic_{args.days}d"
    df.to_csv(f"{stem}.csv", index=False)
    plot_series(df, stem)
    print(f"OK: {stem}.csv, {stem}_price.png, {stem}_volume.png")
