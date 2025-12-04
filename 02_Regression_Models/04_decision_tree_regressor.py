import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree

# ---------------------------------------------------------
# PROJECT: Decision Tree Regressor (Non-Linear Analysis)
# OBJECTIVE: Solve prediction problems where the relationship between variables 
#            is not a straight line (Linear), but complex/rule-based.
# ---------------------------------------------------------

data = {
    "Production_Volume": [120, 130, 90, 105, 140, 85, 115],
    "Defect_Count":  [5,   7,   15,  10,  2,   20,  8]
}
df = pd.DataFrame(data)

X = df[['Production_Volume']]
y = df['Defect_Count']

# Model Training
# Unlike Linear Regression, Decision Trees split data into branches based on rules.
# random_state=42 ensures the tree is built the same way every time.
model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

# Future Prediction
# Scenario: What happens if we produce 200 units?
# Note: Decision Trees often predict the value of the nearest "leaf" node.
new_input = pd.DataFrame([[200]], columns=['Production_Volume'])
prediction = model.predict(new_input)[0]

print(f"\n--- SCENARIO PREDICTION ---")
print(f"Production Volume: 200 Units")
print(f"Predicted Defects: {prediction:.2f}")

# Visualization 1: Model Fit (Actual vs Predicted)
plt.figure(figsize=(10, 5))

# Actual Data (Blue Dots)
plt.scatter(df['Production_Volume'], df['Defect_Count'], color='blue', label='Actual Data', s=100)

# Model Predictions (Red Dots/Lines)
# We predict on the training data to see how well the tree memorized it.
plt.plot(df['Production_Volume'], model.predict(X), color='red', label='Decision Tree Model', linestyle='--', marker='x')

plt.title('Production vs Defects: Decision Tree Fit')
plt.xlabel('Production Volume')
plt.ylabel('Defect Count')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# Visualization 2: The "Brain" of the AI (Tree Structure)
# This plot shows the IF-ELSE rules the model created.
plt.figure(figsize=(12, 8))
plot_tree(model, 
          feature_names=['Production_Volume'],
          filled=True,
          rounded=True,
          fontsize=10)

plt.title("Decision Tree Logic Map (How the decision is made)")
plt.show()