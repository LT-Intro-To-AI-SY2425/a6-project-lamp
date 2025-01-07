import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("")
x = data["Age"]
y = data["GIs"]

plt.figure(figsize=(5,4))

plt.xlabel("Age")
plt.ylabel("")
plt.title(" by Age")
plt.scatter(x, y)

print("Pearson's Correlation: r = :", x.corr(y))

plt.show()