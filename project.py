import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("a6-project-lamp/premier_league_data.csv")
x = data["Age"].values
y = data["GIs"].values

plt.figure(figsize=(5,4))

plt.xlabel("Age")
plt.ylabel("")
plt.title(" by Age")
plt.scatter(x, y)

print("Pearson's Correlation: r = :", x.corr(y))

plt.show()