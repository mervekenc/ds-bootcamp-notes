import pandas as pd
import matplotlib.pyplot as plt

# Analyzes the provided production list, checks against the target, and generates a performance chart.
def analyze_production(production_list, target_value):
    
    # Note: Assumes input list corresponds to Mon-Sun order
    data = {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Production": production_list}
    df = pd.DataFrame(data)
    
    # Calculate Mean
    average_production = df['Production'].mean()

    # Check if average is below target
    if average_production < target_value:
        print(f"ALERT: Average ({average_production:.2f}) is below target ({target_value}).")
    else:
        print(f"SUCCESS: Average ({average_production:.2f}) meets the target ({target_value}).")
    
    plt.figure(figsize=(8, 5))
    plt.bar(df['Day'], df['Production'], label='Daily Production')
    plt.axhline(target_value, color='red', linestyle='--', label='Target Threshold')

    plt.title(f'Weekly Production Analysis (Target: {target_value})')
    plt.xlabel('Days')
    plt.ylabel('Units Produced')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)

    plt.show()

print("--- FACTORY 1 ANALYSIS ---")
factory_1_data = [120, 130, 110, 105, 140, 115, 125]
analyze_production(factory_1_data, target_value=115)

print("\n--- FACTORY 2 ANALYSIS ---")
factory_2_data = [90, 80, 95, 100, 105, 75, 90]
analyze_production(factory_2_data, target_value=100)