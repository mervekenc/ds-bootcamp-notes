import requests
import pandas as pd

"""
API Test Script
---------------
This script simulates a client sending data to the Flask API to get a sales prediction.
"""

# Target URL (Localhost)
url = 'http://127.0.0.1:5000/predict'

# Sample Payload Data
# Manually impute missing values with averages to satisfy the model's requirements.
sample_data = {
    # --- Store Identity ---
    'Store': 1,
    'Dept': 1,
    'Size': 151315,
    'IsHoliday': 0,
    
    # --- Time Features ---
    'Week': 48,           # Early December
    'Year': 2012,
    'Month': 12,
    
    # --- Engineered Features ---
    'Sales_Lag_1': 20000,
    'Sales_Lag_4': 18000,
    'Sales_Lag_52': 19000,
    'Sales_MA4': 19500,
    'Weeks_to_Christmas': 4,
    'Weeks_to_Thanksgiving': 0,

    # --- Macroeconomic Factors (Imputed with Averages) ---
    'Temperature': 45.0,
    'Fuel_Price': 3.4,
    'CPI': 223.0,
    'Unemployment': 6.5,
    
    # --- Markdowns (Set to 0 if unknown) ---
    'MarkDown1': 0.0,
    'MarkDown2': 0.0,
    'MarkDown3': 0.0,
    'MarkDown4': 0.0,
    'MarkDown5': 0.0
}

print("Sending data to server...")

# Send POST Request
try:
    response = requests.post(url, json=sample_data)
    
    # Handle Response
    if response.status_code == 200:
        result = response.json()
        
        if result.get('status') == 'error':
            print("\nSERVER ERROR:")
            print(result.get('message'))
        else:
            print("\nSUCCESS! PREDICTION RECEIVED:")
            print(f"Predicted Weekly Sales: ${result.get('predicted_sales', 'N/A')}")
            
    else:
        print("CONNECTION ERROR!")
        print(f"Status Code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Connection failed: {e}")
    print("Ensure app.py is running in a separate terminal.")