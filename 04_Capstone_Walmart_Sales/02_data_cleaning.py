import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir
df = pd.read_csv(file_path / "merged_raw_data.csv")

# --- Imputation (Filling Missing Values) ---
# Assumption: Missing Markdown values indicate no promotion was active, so we replace NaN with 0.
markdown_col_names = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
df[markdown_col_names] = df[markdown_col_names].fillna(0)

print("Verification - Missing values in MarkDown columns: ")
print(df[markdown_col_names].isnull().sum())

# --- Data Cleaning: Negative Sales ---
# Negative sales usually indicate returns or errors. We filter them out for training.
initial_row_count = df.shape[0]
df = df[df['Weekly_Sales'] >= 0]
dropped_rows = initial_row_count - df.shape[0]

print(f"Dropped {dropped_rows} rows with negative sales ({(dropped_rows/initial_row_count) * 100:.2f}% of data).")

# --- Date Formatting & Feature Engineering ---
# Convert 'Date' column to datetime object
df['Date'] =pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Extract temporal features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week

# Quick inspection
print(f"\nFirst 5 rows of cleaned data: {df.head()}")

# --- Save Cleaned Data ---
output_path = current_dir / 'walmart_cleaned_data.csv'
df.to_csv(output_path, index=False) 

print(f"\nSUCCESS: Cleaned data saved to: {output_path}")