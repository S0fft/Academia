import math

import matplotlib.pyplot as plt
import pandas as pd

SOM = 10

Pt = 13
Gt = 1
Gr = 0
Lt = 0
Lr = 0

channels = {
    "802.11g_ch3": 2422,
    "802.11g_ch11": 2462,
    "802.11n_ch36": 5190,
    "802.11n_ch112": 5570
}

sens_g = {54: -66, 48: -71, 36: -76, 24: -80, 18: -83, 12: -85, 9: -86, 6: -87}
sens_n = {15: -96, 30: -95, 45: -92, 60: -90, 90: -86, 120: -83, 135: -77, 150: -74}


def calc_params(Pmin, F):
    Y = Pt + Gt + Gr - Pmin - Lt - Lr
    FSL = Y - SOM
    D_km = 10 ** (((FSL - 33) / 20) - math.log10(F))
    D_m = round(D_km * 1000, 2)

    return Y, FSL, D_m


results = []

for name, F in channels.items():
    if "g" in name:
        speeds = sens_g
    else:
        speeds = sens_n

    for speed, Pmin in speeds.items():
        Y, FSL, D = calc_params(Pmin, F)
        results.append([name, F, speed, Pmin, round(Y, 2), round(FSL, 2), D])

df = pd.DataFrame(
    results,
    columns=["Channel", "F (MHz)", "Speed (Mbit/s)", "Pmin (dBm)", "Y (dB)", "FSL (dB)", "Distance (m)"]
)

df.to_csv("kharkiv_national_university_of_radio_electronics\pezbm\pz_1\wifi_range_results_full.csv", index=False)

print("\nРезультати збережено у файлі wifi_range_results_full.csv\n")

plt.figure(figsize=(10, 6))

for name in df["Channel"].unique():
    subset = df[df["Channel"] == name].sort_values(by="Speed (Mbit/s)")

    plt.plot(
        subset["Speed (Mbit/s)"],
        subset["Distance (m)"],
        marker="o",
        label=name.replace("_", " ")
    )

plt.title("Залежність дальності від швидкості передачі для каналів 802.11g / 802.11n", fontsize=12)
plt.xlabel("Швидкість передачі, Мбіт/с", fontsize=11)
plt.ylabel("Дальність, м", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Канали", loc="upper right")
plt.tight_layout()

print(df.to_string(index=False))

plt.savefig("kharkiv_national_university_of_radio_electronics\pezbm\pz_1\wifi_range_graph.png", dpi=300)
plt.show()

print("Графік побудовано і збережено як 'wifi_range_graph.png'")
