import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------------
# PROJECT: Time Series Production Trends
# OBJECTIVE: Analyze production trends over time, calculate quality costs,
#            and handle Datetime objects.
# ---------------------------------------------------------

current_dir = Path(__file__).parent
file_path = current_dir / "Production_Data.csv"
df = pd.read_csv(file_path)

# ---------------------------------------------------------
# ANALYSIS 1: Conditional Aggregation
# Business Question: "What is the total production volume for the Day shift?"
# ---------------------------------------------------------
day_shift_production = df[df['Shift'] == "Day"]['UnitsProduced'].sum()
print(f"Total 'Day' Shift Production: {day_shift_production} Units")

# ---------------------------------------------------------
# ANALYSIS 2: Sorting & Ranking
# Identifying the Top 3 worst performing records based on defects.
# ---------------------------------------------------------
top_3_defects = df.sort_values(['DefectCount'], ascending=False).head(3)
print("\n--- TOP 3 HIGHEST DEFECT RECORDS ---")
print(top_3_defects)

# ---------------------------------------------------------
# ANALYSIS 3: Cost Analysis
# Calculating total financial loss due to defects (Assumed Cost: $50 per defect).
# ---------------------------------------------------------
COST_PER_DEFECT = 50
total_loss = df['DefectCount'].sum() * COST_PER_DEFECT
print(f"\nTotal Financial Loss due to Defects: ${total_loss}")

# ---------------------------------------------------------
# ANALYSIS 4: Time Series Handling
# Converting string dates to Python Datetime objects for trend analysis.
# ---------------------------------------------------------
df['Date'] = pd.to_datetime(df['Date'])

# Aggregating daily totals (ignoring shifts)
daily_production = df.groupby('Date')['UnitsProduced'].sum()
print('\n--- DAILY TOTAL PRODUCTION ---')
print(daily_production)

# ---------------------------------------------------------
# ANALYSIS 5: Day-of-Week Analysis
# Extracting day names (Mon, Tue...) to find weekly patterns.
# ---------------------------------------------------------
df['DayName'] = df['Date'].dt.day_name()
avg_production_by_day = df.groupby('DayName')['UnitsProduced'].mean()
print('\n--- AVERAGE PRODUCTION BY DAY OF WEEK ---')
print(avg_production_by_day)

# ---------------------------------------------------------
# VISUALIZATION: Production Trend
# Using a line chart to show fluctuations over time.
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
daily_production.plot(kind='line', linestyle=':', color='red', marker='o')

plt.title('Daily Production Trend')
plt.ylabel('Total Units Produced')
plt.xlabel('Date')
plt.grid(True)
plt.show()