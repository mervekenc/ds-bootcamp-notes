import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PROJECT: Simple Linear Regression (Cost & Efficiency Analysis)
# OBJECTIVE: Understanding the relationship between a single independent variable (X)
#            and a dependent variable (y) using the line equation: y = mx + b
# ---------------------------------------------------------

# ==========================================
# SCENARIO 1: Energy Cost Modelling (Positive Correlation)
# Business Question: "What is our fixed energy cost even if we produce nothing?"
# ==========================================

data_energy = {
    "Production_Units": [100, 200, 300, 400, 500, 600],
    "Energy_Cost": [1200, 1500, 1800, 2100, 2400, 2700]
}
df_energy = pd.DataFrame(data_energy)

x_energy = df_energy[["Production_Units"]]
y_energy = df_energy["Energy_Cost"]

# Model Training
model_energy = LinearRegression()
model_energy.fit(x_energy, y_energy)

# Insight Extraction (Interpreting Coefficients)
variable_cost = model_energy.coef_[0]
fixed_cost = model_energy.intercept_

print(f"Model Equation: y = {variable_cost:.2f}x + {fixed_cost:.2f}")
print(f"Variable Cost per Unit: ${variable_cost:.2f}")
print(f"Fixed Cost: ${fixed_cost:.2f}")

# Future Prediction
# Estimating cost for a hypothetical production volume (1000 units)
future_production = 1000
future_df = pd.DataFrame([[future_production]], columns=['Production_Units'])
predicted_cost = model_energy.predict(future_df)[0]
print(f"Predicted Cost for {future_production} units: ${predicted_cost:.2f}\n")

# ==========================================
# SCENARIO 2: Machine Efficiency (Negative Correlation)
# Maintenance Question: "How much efficiency do we lose for every year of machine age?"
# ==========================================

data_machine = {
    "Machine_Age": [1, 2, 3, 4, 5, 6, 8, 10],
    "Efficiency": [95, 90, 85, 80, 75, 70, 60, 50]
}
df_machine = pd.DataFrame(data_machine)

x_machine = df_machine[['Machine_Age']]
y_machine = df_machine['Efficiency']

# Model Training
model_machine =LinearRegression()
model_machine.fit(x_machine, y_machine)

# Insight Extraction
annual_loss = model_machine.coef_[0]
base_efficiency = model_machine.intercept_

print(f"Base Efficiency (New Machine): {base_efficiency:.2f}%")
print(f"Annual Efficiency Loss: {annual_loss:.2f}%")

# Future Prediction
# Estimating efficiency for an aging machine (15 years old)
prediction_age = pd.DataFrame([[15]], columns=['Machine_Age'])
pred_efficiency = model_machine.predict(prediction_age)
print(f"Prediction: A 15-year-old machine will have {pred_efficiency[0]:.2f}% efficiency.")

# ==========================================
# VISUALIZATION: Side-by-Side Comparison
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Energy Cost
ax1.scatter(df_energy['Production_Units'], df_energy['Energy_Cost'], color='blue', label='Actual Data')
ax1.plot(df_energy['Production_Units'], model_energy.predict(x_energy), color='red', linewidth=2, label='Regression Line')
ax1.set_title('Scenario 1: Energy Cost')
ax1.set_xlabel('Production_Units')
ax1.set_ylabel('Energy_Cost')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)

# Plot 2: Machine Efficiency
ax2.scatter(df_machine['Machine_Age'], df_machine['Efficiency'], color='green', label='Actual Data')
ax2.plot(df_machine['Machine_Age'], model_machine.predict(x_machine), color='orange', linewidth=2, label='Depreciation Trend')
ax2.set_title('Scenario 2: Machine Efficiency')
ax2.set_xlabel('Machine Age (Years)')
ax2.set_ylabel('Efficiency (%)')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()