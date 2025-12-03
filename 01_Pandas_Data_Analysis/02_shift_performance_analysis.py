import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "Production_Data.csv"
df = pd.read_csv(file_path)

df['DefectRate'] = df['DefectCount'] / df['UnitsProduced'] 
print(df)

# Filter records where error count > 10
critical_shifts = df[df['DefectCount'] > 10]
print("--- CRITICAL SHIFTS (Defect Count > 10) ---")
print(critical_shifts)

print("\n--- SHIFT PERFORMANCE ANALYSIS (Pivot Table) ---")
shift_summary = df.groupby('Shift')[['DefectCount', 'UnitsProduced', 'DefectRate']].mean()
print(shift_summary)

shift_summary['DefectRate'].plot(kind='bar', color=['orange', 'purple', 'teal'], rot=0)

plt.title('Shift-wise Defect Rate Comparison')
plt.ylabel('Defect Rate')
plt.xlabel('Shift')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()