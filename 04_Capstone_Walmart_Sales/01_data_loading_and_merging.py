import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir

# --- Data Loading ---
df_features = pd.read_csv(file_path / "features.csv")
df_train = pd.read_csv(file_path / "train.csv")
df_stores = pd.read_csv(file_path / "stores.csv")

# --- Validation: Check 'IsHoliday' consistency before merging ---
# Perform an inner join to check if 'IsHoliday' flags match in both datasets for the same Store/Date.
merge_validation = pd.merge(df_train, df_features, on=['Store', 'Date'], how='inner')
is_holiday_consistent = (merge_validation['IsHoliday_x'] == merge_validation['IsHoliday_y']).all()
print(f"Validation - All IsHoliday columns match: {is_holiday_consistent}")

# --- Pre-processing ---
# Drop 'IsHoliday' from features to prevent duplicate columns after merge
df_features_clean = df_features.drop(columns = ['IsHoliday'])

# --- Merging Data ---
# 1. Merge Train + Stores (Many-to-One relationship)
df_train_stores_merged = pd.merge(df_train, df_stores, on='Store', how='left', validate='m:1')

# 2. Merge Result + Features (Many-to-One relationship based on Store and Date)
df_merged = pd.merge(df_train_stores_merged, df_features_clean, on=['Store', 'Date'], how='left', validate='m:1')
print(f"Columns after merge: {df_merged.columns.tolist()}")

# --- Post-Merge Checks ---
print(f"Final Table Shape: {df_merged.shape}")

missing_values = df_merged.isnull().sum()
print(f"Missing values in each column: \n{missing_values}")

# Uniqueness Checks
# Note: 'Store' is NOT unique in features/train (repeated over time), but MUST be unique in stores.csv
print(f"Is 'Store' unique in Features? {df_features['Store'].is_unique} (Expected: False)")
print(f"Is 'Store' unique in Train? {df_train['Store'].is_unique} (Expected: False)")
print(f"Is 'Store' unique in Stores? {df_stores['Store'].is_unique} (Expected: True)")

# --- Save Semi-Finished Data ---
output_path = current_dir / 'merged_raw_data.csv'
df_merged.to_csv(output_path, index=False) 

print(f"\nSUCCESS: Merged data saved to: {output_path}")