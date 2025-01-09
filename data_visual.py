import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("premier-player-23-24.csv")
x_1 = data["Age"]
x_2 = data["Min"]
x_3 = data["90s"]
y = data["Gls"]

fig, graph = plt.subplots(3)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Age")
graph[0].set_ylabel("Gls")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Min")
graph[1].set_ylabel("Gls")

graph[2].scatter(x_3, y)
graph[2].set_xlabel("90s")
graph[2].set_ylabel("Gls")

print("Correlation between Age and Gls: ", round(x_1.corr(y),2))
print("Correlation between Min and Gls: ", round(x_2.corr(y),2))
print("Correlation between 90s and Gls: ", round(x_3.corr(y),2))

plt.tight_layout()
plt.show()