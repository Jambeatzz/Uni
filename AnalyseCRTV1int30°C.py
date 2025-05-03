import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


corrected_time = [0, 0.5, 1, 1.5, 2, 2.5, 3] + list(range(4, 21))

conductivity = [
    7.61, 7.16, 6.53, 6.02, 5.65, 5.35, 5.11, 4.74, 4.47, 4.27,
    4.11, 3.99, 3.88, 3.79, 3.72, 3.66, 3.60, 3.55, 3.50, 3.46,
    3.43, 3.40, 3.37, 3.34
]



CA_0 = 0.04  
CA_inf = 0     
W_0 = 7.61
W_inf = 2.67

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

df.to_csv("Daten für die gesamte berechnung von Integralmethode bei 30°C.csv")



plt.figure(figsize=(10, 6))
plt.plot(corrected_time, cabytwo, marker='x', linestyle='-', color='blue')
plt.title("Konzentrations-Zeit-Diagramm 30°C")
plt.xlabel("Zeit [min], m und b für Lineare Regression:  " + f"{curve}" +"    R^2: 0,9983")
plt.ylabel("1/Konzentration - 1/Konzentration zu 0")
plt.grid(True)
plt.tight_layout()
plt.show()


