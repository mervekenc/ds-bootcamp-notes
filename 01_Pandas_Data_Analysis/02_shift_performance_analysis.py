import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------------------------------------
# PROJECT: Shift Performance Analysis
# OBJECTIVE: Compare operational efficiency between Day and Night shifts
#            using aggregated metrics and defect rates.
# ---------------------------------------------------------

# 1. Data Ingestion
# Using pathlib for cross-platform compatibility (works on Windows/Mac/Linux).
current_dir = Path(__file__).parent
file_path = current_dir / "Production_Data.csv"
df = pd.read_csv(file_path)

# 2. KPI Calculation: Defect Rate
# Defect Rate = (Defect Count / Total Units Produced)
# This metric is crucial for Quality Control (QC).
df['DefectRate'] = df['DefectCount'] / df['UnitsProduced'] 
print(df)

# 3. Anomaly Detection (Rule-Based)
# Identifying specific shifts where defect count exceeded the safety threshold (10).
critical_shifts = df[df['DefectCount'] > 10]
print("--- CRITICAL SHIFTS (Defect Count > 10) ---")
print(critical_shifts)

# 4. Aggregation (Pivot Analysis)
# Grouping data by 'Shift' to compare average performance.
print("\n--- SHIFT PERFORMANCE ANALYSIS (Pivot Table) ---")
shift_summary = df.groupby('Shift')[['DefectCount', 'UnitsProduced', 'DefectRate']].mean()
print(shift_summary)

# 5. Visualization
# Comparing Defect Rates to identify the problematic shift.
shift_summary['DefectRate'].plot(kind='bar', color=['orange', 'purple', 'teal'], rot=0)

plt.title('Shift-wise Defect Rate Comparison')
plt.ylabel('Defect Rate')
plt.xlabel('Shift')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()