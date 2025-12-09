import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "walmart_cleaned_data.csv"
df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Set visual style
sns.set_theme(style="whitegrid")

# ==========================================
# 1. VISUALIZATION: Sales Over Time
# ==========================================
# Group data by Date to see the total trend
daily_sales = df.groupby('Date')['Weekly_Sales'].sum()

plt.figure(figsize=(15, 5))
plt.plot(daily_sales.index, daily_sales.values, color='tab:blue')

# ==========================================
# CRITICAL DATASET NOTE: THE "FRIDAY" RULE
# ==========================================
# The 'Date' column in this dataset represents the FRIDAY that ends the week.
# It does NOT represent the actual day of the holiday.
# Walmart reports sales weekly from Saturday to Friday.
#
# Logic: If a holiday falls within the week (Sat-Fri), 
# the 'IsHoliday' flag is set to True for that Friday's date.
special_dates = {
    'Super Bowl':   ['2010-02-12', '2011-02-11', '2012-02-10'],
    'Labor Day':    ['2010-09-10', '2011-09-09', '2012-09-07'],
    'Thanksgiving': ['2010-11-26', '2011-11-25'],
    'Christmas':    ['2010-12-31', '2011-12-30']
}
# Since the holiday flag is on the week-ending date, the actual shopping spike
# (e.g., buying gifts) might appear in the week BEFORE the flagged date.
# Keep this lag in mind during analysis!
# ==========================================


holiday_colors = {
    'Super Bowl': 'green',
    'Labor Day': 'blue',
    'Thanksgiving': 'orange',
    'Christmas': 'red'
}
for holiday_name, dates_list in special_dates.items():
    for date_str in dates_list:
        target_date = pd.to_datetime(date_str)

        if (target_date >= daily_sales.index.min()) and (target_date <= daily_sales.index.max()):
            # Draw the vertical line
            plt.axvline(x=target_date, color=holiday_colors[holiday_name], linestyle='--', alpha=0.6)
            # Add the text label
            plt.text(x=target_date, y=daily_sales.max()*0.90, s=holiday_name, rotation=90, color=holiday_colors[holiday_name], fontsize=9, fontweight='bold')


plt.title('Total Weekly Sales Over Time', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()

# Print top 5 sales dates
print("Top 5 Dates with Highest Sales:")
print(daily_sales.sort_values(ascending=False).head(5))

# ==========================================
# 2. VISUALIZATION: Holiday vs. Non-Holiday
# ==========================================

# --- Plot A: Boxplot (Statistical Summary & Outliers) ---
plt.figure(figsize=(10, 6))
# Fix: Added hue='IsHoliday' and legend=False to prevent FutureWarning
sns.boxplot(x='IsHoliday', y='Weekly_Sales', data=df, hue='IsHoliday', legend=False, palette="Set2")
plt.title("Sales Statistics: Holiday vs Non-Holiday")
plt.xlabel("Is Holiday?")
plt.ylabel("Weekly Sales ($)")
plt.show()

# --- Plot B: Barplot (Average Comparison with Annotation) ---
plt.figure(figsize=(8, 6))
# Fix: Added hue='IsHoliday' and legend=False to prevent FutureWarning
# ci=None removes the confidence interval bars for a cleaner look
ax = sns.barplot(x='IsHoliday', y='Weekly_Sales', data=df, hue='IsHoliday', legend=False, palette="Set2", errorbar=None)

plt.title("Average Sales: Holiday vs Non-Holiday")
plt.xlabel("Is Holiday?")
plt.ylabel("Average Weekly Sales ($)")

# Annotate bars with the exact numbers
for p in ax.patches:
    ax.annotate(f'${p.get_height():,.0f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), 
                textcoords='offset points',
                fontweight='bold')
plt.show()