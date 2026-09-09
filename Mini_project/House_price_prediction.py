# House Price Prediction using Simple Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Area": [500, 600, 700, 800, 900,
             1000, 1100, 1200, 1300, 1400],

    "Price": [25, 30, 35, 40, 45,
              50, 55, 60, 65, 70]
}

df = pd.DataFrame(data)


print("House Price Dataset:")
print(df)


X = df[["Area"]]
y = df["Price"]


model = LinearRegression()


model.fit(X, y)


print("\nRegression Equation:")
print("Price =", model.intercept_, "+",
      model.coef_[0], "* Area")


area = float(input("\nEnter house area in sq ft: "))


predicted_price = model.predict([[area]])

print("Predicted House Price:",
      predicted_price[0], "lakh")


plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X),
         color="red", label="Regression Line")

plt.xlabel("House Area (sq ft)")
plt.ylabel("House Price (₹ lakh)")
plt.title("House Price Prediction")
plt.legend()
plt.show()