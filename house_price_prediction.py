import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("Housing.csv")

print("\nDataset Shape:", data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

plt.figure(figsize=(8, 6))
sns.heatmap(
    data[["price", "area", "bedrooms", "bathrooms"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=data["area"], y=data["price"])
plt.title("Area vs House Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

X = data[["area", "bedrooms", "bathrooms"]]
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n===== MODEL EVALUATION =====")
print("Mean Absolute Error :", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error  :", mean_squared_error(y_test, y_pred))
print("R2 Score            :", r2_score(y_test, y_pred))

plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)
plt.show()

residuals = y_test - y_pred

plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Predicted Price")
plt.ylabel("Residual Error")
plt.title("Residual Error Plot")
plt.show()

print("\n===== HOUSE PRICE PREDICTION =====")

area = float(input("Enter Area (sq ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
bathrooms = int(input("Enter Number of Bathrooms: "))

new_house = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms]
})

predicted_price = model.predict(new_house)

print("\nPredicted House Price: ₹{:,.2f}".format(predicted_price[0]))