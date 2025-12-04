import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# ---------------------------------------------------------
# PROJECT: Regression Model Evaluation
# OBJECTIVE: Validate the performance of a Linear Regression model using
#            Train-Test Split and metrics like MAE and R-Squared.
# ---------------------------------------------------------

data = {
    "Production_Volume":    [120, 130, 90, 105, 140, 85, 115, 100, 110, 125, 95, 135],
    "Defect_Count":         [5,   7,   15, 10,  2,   20, 8,   12,  9,   6,   14, 3]
}
df = pd.DataFrame(data)

x = df[["Production_Volume"]]
y = df["Defect_Count"]

# Train-Test Split
# Splitting the dataset: 80% for Training (Learning), 20% for Testing (Exam).
# This creates a realistic simulation where the model faces unseen data.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Total Dataset Size: {len(df)}")
print(f"Training Set Size:  {len(x_train)}") 
print(f"Test Set Size:      {len(x_test)}")

# Model Training
model = LinearRegression()
model.fit(x_train, y_train)

# 4. Model Evaluation (Testing)
y_pred = model.predict(x_test)

print("\n--- PREDICTION RESULTS (Test Set) ---")

# Create a comparison DataFrame for better readability
results = pd.DataFrame({
    'Actual_Defects': y_test.values,
    'Predicted_Defects': y_pred,
    'Difference': y_test.values - y_pred
})
print(results)

# Performance Metrics
print("\n--- PERFORMANCE METRICS REPORT ---")

# Mean Absolute Error (MAE): The average size of mistakes.
# "On average, how many units is the model off by?"
mae = mean_absolute_error(y_test, y_pred)
print(f"Interpretation: On average, the prediction deviates by {mae:.2f} defects.")

# R-Squared (R2): The proportion of variance explained by the model.
# "How well does the model fit the data?" (1.0 is perfect, 0.0 is poor)
r2 = r2_score(y_test, y_pred)

print(f"R² Score: {r2:.2f} ({r2*100:.1f}%)")
print(f"Interpretation: The model explains {r2*100:.1f}% of the variability in defect counts.")