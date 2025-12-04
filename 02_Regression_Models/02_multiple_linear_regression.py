import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PROJECT: Clean Room Energy Analysis (Multivariable Regression)
# OBJECTIVE: Analyze the impact of production volume, temperature, and 
#            active machinery on energy costs using Multiple Linear Regression.
# ---------------------------------------------------------

dataset = {
    'Month':            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    'Production_Qty':   [1000, 1200, 1500, 1100, 1600, 1800, 1700, 1900],
    'Temperature_C':    [5, 8, 12, 18, 25, 30, 35, 32],
    'Active_Machines':  [2, 2, 3, 2, 4, 4, 4, 5],
    'Energy_Bill':      [3500, 3900, 4800, 4200, 5800, 6500, 6800, 7200]
}
df = pd.DataFrame(dataset)

x = df[['Production_Qty', 'Temperature_C', 'Active_Machines']]
y = df['Energy_Bill']

# Model Training
model = LinearRegression()
model.fit(x, y)

# Insight Extraction (Coefficients)
production_cost = model.coef_[0]
temp_cost = model.coef_[1]
machine_cost = model.coef_[2]
base_cost = model.intercept_

print("--- FACTOR IMPACT ANALYSIS ---")
print(f"Model Equation: Bill = {production_cost:.2f}*Prod + {temp_cost:.2f}*Temp + {machine_cost:.2f}*Mach + {base_cost:.2f}")
print(f"Cost per Unit Produced: ${production_cost:.2f}")
print(f"Cost per Degree (Temp): ${temp_cost:.2f}")
print(f"Cost per Active Machine: ${machine_cost:.2f}")
print(f"Base Fixed Cost: ${base_cost:.2f}")

# Future Prediction
# Scenario: 2000 units, 28°C temperature, 5 active machines
future_conditions = pd.DataFrame([[2000, 28, 5]], columns=['Production_Qty', 'Temperature_C', 'Active_Machines'])
predicted_bill = model.predict(future_conditions)[0]
print(f"Conditions: 2000 Units, 28°C, 5 Machines")
print(f"Predicted Energy Bill: ${predicted_bill:.2f}")

# Visualization (Actual vs Predicted)
# Generate predictions for the entire dataset to compare with actuals
predictions = model.predict(x)

plt.figure(figsize=(9, 6))

# Scatter plot for actual data points
plt.scatter(y, predictions, color='blue', s=100, alpha=0.7, label='Data Points')

# Perfect prediction line (y = x)
min_val = min(y.min(), predictions.min())
max_val = max(y.max(), predictions.max())
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', linewidth=2, label='Perfect Prediction (y=x)')

plt.title('Actual vs Predicted Energy Bill')
plt.xlabel('Actual Bill ($)')
plt.ylabel('Predicted Bill ($)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()