import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Production": [120, 130, 90, 105, 140, 85, 115],
}
df = pd.DataFrame(data)

TARGET_VALUE = 110

# Calculate Deviation from Target
df['Deviation'] = df['Production'] - TARGET_VALUE

days_below_target = df[df['Production'] < TARGET_VALUE]
print("--- DAYS BELOW TARGET (< 110) ---")
print(days_below_target)

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

print("\n--- PRODUCTION DATA TABLE ---")
print(df)

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

