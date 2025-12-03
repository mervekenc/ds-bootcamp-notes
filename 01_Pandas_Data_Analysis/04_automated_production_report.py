import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PROJECT: Automated Production Reporting Tool
# OBJECTIVE: Create a reusable function to generate standardized 
#            production reports for multiple factories.
# ---------------------------------------------------------

def analyze_production(production_list, target_value):
    """
    Analyzes weekly production data, prints status alerts, 
    and generates a performance chart.
    
    Args:
        production_list (list): List of daily production integers.
        target_value (int): The KPI target threshold.
    """
    
    # Create DataFrame from input list
    data = {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Production": production_list}
    df = pd.DataFrame(data)
    
    # Calculate Average KPI
    average_production = df['Production'].mean()

    # Decision Logic: Check if performance meets the target
    print(f"\n--- ANALYSIS REPORT (Target: {target_value}) ---")
    if average_production < target_value:
        print(f"ALERT: Weekly Average ({average_production:.2f}) is BELOW target ({target_value}).")
    else:
        print(f"SUCCESS: Average ({average_production:.2f}) MEETS the target ({target_value}).")
    
    # Visualization
    plt.figure(figsize=(8, 5))
    plt.bar(df['Day'], df['Production'], label='Daily Production')
    plt.axhline(target_value, color='red', linestyle='--', linewidth=2, label='Target Threshold')

    plt.title(f'Production Performance Analysis (Target: {target_value})')
    plt.xlabel('Day')
    plt.ylabel('Units Produced')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()

# --- SIMULATION: Running the tool for different factories ---

# Scenario 1: High Performing Factory
print("Processing Factory A Data...")
factory_a_data = [120, 130, 110, 105, 140, 115, 125]
analyze_production(factory_a_data, target_value=115)

# Scenario 2: Low Performing Factory
print("\nProcessing Factory B Data...")
factory_b_data = [90, 80, 95, 100, 105, 75, 90]
analyze_production(factory_b_data, target_value=100)