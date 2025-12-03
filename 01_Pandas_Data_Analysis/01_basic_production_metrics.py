import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PROJECT: Basic Production Metrics Analysis
# OBJECTIVE: Analyze weekly production data using manual data entry
#            to understand deviation from target goals.
# ---------------------------------------------------------

# 1. Data Creation (Manual Dictionary)
# Simulating raw production data for a single week.

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Production": [120, 130, 90, 105, 140, 85, 115],
}
df = pd.DataFrame(data)

# Define Key Performance Indicator (KPI) Target
TARGET_VALUE = 110

# 2. Feature Engineering
# Calculating 'Deviation' to quantify how much we missed or exceeded the target.
df['Deviation'] = df['Production'] - TARGET_VALUE

# 3. Filtering Critical Days
# Identifying days where production fell below the acceptable threshold.
days_below_target = df[df['Production'] < TARGET_VALUE]
print("--- DAYS BELOW TARGET (< 110) ---")
print(days_below_target)

# 4. Visualization with Conditional Logic
# Bars are colored RED if below target, SKYBLUE if above target.
colors = ['red' if x < TARGET_VALUE else 'skyblue' for x in df['Production']]
plt.figure(figsize=(10, 6))
plt.bar(df['Day'], df['Production'], color=colors)
plt.axhline(TARGET_VALUE, color='red', linestyle='--', label=f'Target ({TARGET_VALUE})')

plt.title("Weekly Production Performance")
plt.xlabel("Day")
plt.ylabel("Production Units")
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.show()

# 5. Summary Statistics
print("\n--- PRODUCTION DATA TABLE ---")
print(df)

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

