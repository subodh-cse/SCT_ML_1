# SCT_ML_1 - House Price Prediction Using Linear Regression

# Project Overview

This project implements a Linear Regression model to predict house prices based on the following features:

* Area (Square Feet)
* Number of Bedrooms
* Number of Bathrooms

The model is trained using the House Price Dataset and predicts the price of a house based on user-provided inputs.


# Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn



# Features

* Data Loading and Preprocessing
* Data Visualization
* Correlation Heatmap
* Linear Regression Model
* Actual vs Predicted Price Comparison
* Model Evaluation
* House Price Prediction Using User Input



# Dataset

The project uses the House Price Dataset containing information such as:

* Price
* Area
* Bedrooms
* Bathrooms



# Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values. In this project, it is used to estimate house prices based on selected features.



# Data Visualization

The project includes the following visualizations:

1. Correlation Heatmap
2. Area vs House Price Scatter Plot
3. Actual vs Predicted Price Plot
4. Residual Error Plot

These visualizations help in understanding the dataset and evaluating model performance.


# Model Evaluation Metrics

The model is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score



# Project Structure


SCT_ML_1/
│
├── house_price_prediction.py
├── Housing.csv
├── requirements.txt
└── README.md


---

# Installation

Clone the repository:

```bash
git clone https://github.com/subodh-cse/SCT_ML_1.git
```

Move into the project directory:

```bash
cd SCT_ML_1
```

Install the required libraries:

```bash
pip install -r requirements.txt
```


# Run the Project

```bash
python house_price_prediction.py
```



# Sample Input

```text
Enter Area (sq ft): 2500
Enter Number of Bedrooms: 3
Enter Number of Bathrooms: 2
```


# Sample Output

```text
Predicted House Price: ₹5,421,856.43
```


# Future Improvements

* Add more housing features
* Compare multiple regression algorithms
* Build a web application using Flask
* Deploy the model online


# Conclusion

This project demonstrates the implementation of Linear Regression for predicting house prices using area, bedrooms, and bathrooms. It also includes data visualization and model evaluation techniques to analyze prediction performance.


# Author

Subodh

## Output Screenshots

### Correlation Heatmap

![Heatmap](Correlation%20Heatmap.png)

### Area vs House Price

![Area vs Price](Area%20vs%20House%20price.png)

### Actual vs Predicted Price

![Actual vs Predicted](Actual%20vs%20Predicted%20Price.png)

### Residual Error Plot

![Residual Plot](Residual%20Error%20Plot.png)


