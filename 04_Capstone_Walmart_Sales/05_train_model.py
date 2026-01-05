import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from matplotlib import pyplot as plt

current_dir = Path(__file__).parent
df = pd.read_csv(current_dir / "final_train_data.csv", parse_dates=['Date'])
plot_save_path = current_dir / "model_performance_plot.png"

# Convert boolean to int
if 'IsHoliday' in df.columns:
    df['IsHoliday'] = df['IsHoliday'].astype(int)

# --- TIME BASED SPLIT ---
# Cutoff: Feb 2012
# Train on past data (2010-2012) and test on future data (2012-Oct)
split_date = '2012-02-01'

train_df = df[df['Date'] < split_date]
test_df = df[df['Date'] >= split_date]

# Define Features (X) and Target (y)
# Exclude 'Weekly_Sales' (Target), 'Date' (Non-numeric) and 'Type' (Categorical)
drop_cols = ['Weekly_Sales', 'Date', 'Type']

X_train = train_df.drop(columns = drop_cols, errors='ignore').select_dtypes(include=['number'])
y_train = train_df['Weekly_Sales']

X_test = test_df.drop(columns = drop_cols, errors='ignore').select_dtypes(include=['number'])
y_test = test_df['Weekly_Sales']

print(f"Training Data: {X_train.shape[0]} rows (Feb 2010 - Feb 2012)")
print(f"Test Data    : {X_test.shape[0]} rows (Feb 2012 - Oct 2012)")
print(f"Features Used: {X_train.columns.tolist()}")

# --- MODEL TRAINING ---
model = RandomForestRegressor(n_estimators=100, n_jobs=-1, random_state=42)
model.fit(X_train, y_train)

print("Model Trained Successfully!")

# --- MODEL EVALUATION ---
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"PERFORMANCE REPORT:")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"R² Score (Accuracy)      : {r2:.4f}")

# --- VISUALIZATION ---
# Plotting first 150 samples to compare Actual vs Predicted
plt.figure(figsize=(15, 6))
plt.plot(y_test.values[:150], label='Actual Sales', color='blue', alpha=0.7)
plt.plot(y_pred[:150], label='Predicted Sales', color='red', linestyle='--', alpha=0.7)

plt.title('Actual vs Predicted Sales (Feb 2012 - Onwards)')
plt.xlabel('Sample Index')
plt.ylabel('Weekly Sales ($)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig(plot_save_path)
print(f"Performance plot saved to: {plot_save_path}")

plt.show()

# --- FEATURE IMPORTANCE ---
# Identify which features drove the decisions
importances = pd.Series(model.feature_importances_, index=X_train.columns)
print("\nTop 5 Most Important Features:")
print(importances.sort_values(ascending=False).head(5))