import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


corrected_time = [0, 0.5, 1, 1.5, 2, 2.5, 3] + list(range(4, 31))

conductivity = [
    15.92/2, 7.66, 7.19, 6.83, 6.50, 6.22, 5.99, 5.59, 5.28, 5.04, 4.84,
    4.67, 4.53, 4.41, 4.30, 4.21, 4.13, 4.05, 3.99, 3.93, 3.87, 3.83, 3.78,
    3.74, 3.70, 3.67, 3.63, 3.60, 3.57, 3.54, 3.52, 3.49, 3.47, 3.45
]



CA_0 = 0.04  
CA_inf = 0     
W_0 = 15.92/2
W_inf = 2.65

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

df.to_csv("Daten für die gesamte berechnung von Integralmethode.csv")



plt.figure(figsize=(10, 6))
plt.plot(corrected_time, cabytwo, marker='x', linestyle='-', color='blue')
plt.title("Konzentrations-Zeit-Diagramm")
plt.xlabel("Zeit [min], m und b  für den linearen Durchschnitt: " + f"{curve}" + "    R^2: 0.999")
plt.ylabel("1/Konzentration - 1/Konzentration zu 0")
plt.grid(True)
plt.tight_layout()
plt.show()

