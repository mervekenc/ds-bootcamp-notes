import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "Production_Data.csv"
df = pd.read_csv(file_path)
print(df)

# ---------------------------------------------------------
# TASK 1: Total Production in 'Day' Shift
# Manager's Request: "Tell me the total units produced only in the Day shift."
# ---------------------------------------------------------

day_shift_data = df[df['Shift'] == "Day"]
total_day_production = day_shift_data['UnitsProduced'].sum()

print(f"\nTotal Production in 'Day' Shift: {total_day_production}")

# ---------------------------------------------------------
# TASK 2: Identify Top 3 Problematic Shifts
# List the top 3 shifts with the highest defects.
# ---------------------------------------------------------

sorted_by_defects = df.sort_values(['DefectCount'], ascending=False)
top_3_defects = sorted_by_defects.head(3)
print("\n--- Top 3 Shifts with Highest Defects ---")
print(top_3_defects)

# ---------------------------------------------------------
# TASK 3: Calculate Total Defect Cost
# Cost per defect is 50 USD.
# ---------------------------------------------------------

COST_PER_DEFECT = 50
total_defect_cost = (df['DefectCount'].sum()) * COST_PER_DEFECT
print(f"Total Defect Cost for the Week: {total_defect_cost} USD")

# ---------------------------------------------------------
# TASK 4: Data Type Conversion & Daily Totals
# Manager's Request: "Ignore shifts, show me total daily production."
# ---------------------------------------------------------

df['Date'] = pd.to_datetime(df['Date'])
print("\nData Types Updated.")
df.info()

daily_total_production = df.groupby('Date')['UnitsProduced'].sum()
print('\n--- Total Production by Date ---')
print(daily_total_production)

# ---------------------------------------------------------
# TASK 5: Average Production by Day Name
# Create a 'DayName' column and group by it.
# ---------------------------------------------------------

df['DayName'] = df['Date'].dt.day_name()
print("\n--- Data with Day Names ---")
print(df[['Date', 'DayName']].head())

avg_production_by_day = df.groupby('DayName')['UnitsProduced'].mean()
print('\n--- Average Production by Day Name ---')
print(avg_production_by_day)

# ---------------------------------------------------------
# VISUALIZATION: Line Plot for Daily Production
# ---------------------------------------------------------

daily_total_production.plot(kind='line', linestyle = ':', color = 'red', marker = 'o')

plt.title('Daily Total Production Trend')
plt.ylabel('Units Produced')
plt.xlabel('Date')
plt.show()