import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#datensätze zeit und conductivity
corrected_time = [0, 0.5, 1, 1.5, 2, 2.5, 3] + list(range(4, 31))

conductivity = [
    15.92/2, 7.66, 7.19, 6.83, 6.50, 6.22, 5.99, 5.59, 5.28, 5.04, 4.84,
    4.67, 4.53, 4.41, 4.30, 4.21, 4.13, 4.05, 3.99, 3.93, 3.87, 3.83, 3.78,
    3.74, 3.70, 3.67, 3.63, 3.60, 3.57, 3.54, 3.52, 3.49, 3.47, 3.45
]


#daten aus messungen zur berechnung
CA_0 = 0.04  
CA_inf = 0     
W_0 = 15.92/2
W_inf = 2.65

CA_t = [(W - W_inf) / (W_0 - W_inf) * (CA_0 - CA_inf) + CA_inf for W in conductivity]

diff = [i - j for i,j in zip(CA_t, CA_t[1:])]
difft = [i - j for i,j in zip(corrected_time, corrected_time[1:])]


#hier wird -r logarithmiert
listr = np.log(-np.array(diff)/np.array(difft))


caneu = CA_t[:-1]

#hier habe ich erst mit **2 und dann mit llog für den natürlichen logarithmus die konzentration logarithmiert
caneusq = np.log(np.array(caneu))

#zum test
print(f"{CA_t}")


#hier wird die lineare regression berechnet 
curve = np.polyfit(caneusq[1:], listr[1:], 1)



#hier habe ich die kurve zeichnen lassen

plt.figure(figsize=(10, 6))
plt.plot(caneusq[1:], listr[1:], marker='x', linestyle='-', color='blue')
plt.title("Konzentrations-Geschwindigkeits-Diagramm")
plt.xlabel("ln(C), m und b für lineare regression:  "+f"{curve}"+"   R^2: 0.9934")
plt.ylabel("ln(r)")
plt.grid(True)
plt.tight_layout()
plt.show()





#für den export in ein csv file
data = {
    "fa" : caneusq[1:],
    "r" : listr[1:]
}



#für den export in ein csv file
df = pd.DataFrame(data)

df.to_csv("/Users/jordihohmann/Desktop/Integralmethode/diffslndata.csv")
