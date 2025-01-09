import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("premier-player-23-24.csv")
x = data[["Age", "Min", "90s"]].values
y = data["Gls"].values

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

model = LinearRegression().fit(xtrain, ytrain)
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_))
r_squared = round(model.score(x, y), 2)

print(f"Model's Linear Equation: y={coef[0]}x1 + {coef[1]}x2 + {coef[2]}x3 + {intercept}")
print("R Squared Value: ", r_squared)

predict = model.predict(xtest)
predict = np.around(predict, 2)
print(predict)

print("\nTesting Multivariable Model With Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print(f"Age: {x_coord[0]} Minutes Played: {x_coord[1]} Num of 90 Min Games: {x_coord[2]} Actual: {actual} Predicted {predicted_y}")