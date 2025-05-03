import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


corrected_time = [0, 0.5, 1, 1.5, 2, 2.5, 3] + list(range(4, 21))

conductivity = [
    7.33, 6.46, 5.60, 5.12, 4.78, 4.54, 4.34, 4.05, 3.85, 3.72,
    3.60, 3.52, 3.45, 3.39, 3.34, 3.30, 3.27, 3.24, 3.22, 3.19,
    3.17, 3.15, 3.14, 3.13
]




CA_0 = 0.04  
CA_inf = 0     
W_0 = 7.33
W_inf = 2.68

CA_t = [(W - W_inf) / (W_0 - W_inf) * (CA_0 - CA_inf) + CA_inf for W in conductivity]

Caln = np.log(np.array(CA_t)/CA_0)

cabytwo = (1/np.array(CA_t))-(1/CA_0)

curve = np.polyfit(corrected_time, cabytwo, 1)


assert len(corrected_time) == len(conductivity)


data = {
    "time":corrected_time,
    "konz":CA_t,
    "berechn. 1.ordnung":Caln,
    "berechn. 2. ordnung": cabytwo
}

df = pd.DataFrame(data)

df.to_csv("Daten für die gesamte berechnung von Integralmethode bei 40°C.csv")



plt.figure(figsize=(10, 6))
plt.plot(corrected_time, cabytwo, marker='x', linestyle='-', color='blue')
plt.title("Konzentrations-Zeit-Diagramm 40°C")
plt.xlabel("Zeit [min], m und b für lineare regression:  "+f"{curve}" + "   R^2: 0.9914")
plt.ylabel("ln(Konzentration/Konzentration zu 0)")
plt.grid(True)
plt.tight_layout()
plt.show()


