import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("demo/demo_series.csv")

# Цена с отметками аномалий
ax = df["price"].plot()
ax.set_title("Synthetic Price")
ax.set_xlabel("step")
ax.set_ylabel("price")
an_idx = df.index[df["anomaly"]]
ax.plot(an_idx, df.loc[an_idx, "price"], "o", markersize=4)
plt.tight_layout()
plt.savefig("demo/price_plot.png")
plt.show()

# Объём
plt.figure()
df["volume"].plot()
plt.title("Synthetic Volume")
plt.xlabel("step")
plt.ylabel("volume")
plt.tight_layout()
plt.savefig("demo/volume_plot.png")
plt.show()
