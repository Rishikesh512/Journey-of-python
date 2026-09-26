# House Price Prediction using Simple Linear Regression

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv("./house.csv")


# 2. Display dataset
print("House Price Dataset:")
print(df)

# 3. Separate input and output
X = df.drop("price_lakhs", axis=1)
y = df["price_lakhs"]

# Spliting the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(type(X_test))
# 4. Create model
model = LinearRegression()

# 5. Train model
model.fit(X_train, y_train)

# 6. Display equation
print("\nRegression Equation:")

print(
    f"Price = {model.intercept_:.2f} "
    f"+ ({model.coef_[0]:.4f} × Area) "
    f"+ ({model.coef_[1]:.4f} × Bedrooms) "
    f"+ ({model.coef_[2]:.4f} × Bathrooms) "
    f"+ ({model.coef_[3]:.4f} × Age) "
    f"+ ({model.coef_[4]:.4f} × Location Score)"
)

# 7. Take input from user
area_sqft = float(input("\nEnter house area in sq ft: "))
bedrooms = int(input("\nEnter number of bedrooms:"))
bathrooms = int(input("\nEnter number of bathrooms:"))
age_years =  float(input("\nEnter number of years:"))
location_score = int(input("\nEnter number location_score:"))

X_input = np.array([[area_sqft, bedrooms, bathrooms, age_years, location_score]])


print("Input values: ",X_input)
predicted_price = model.predict(X_input)

print(f"Predicted House Price: {predicted_price[0]:.2f} lakh")
