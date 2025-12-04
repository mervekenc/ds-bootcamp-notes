# Industrial Engineer to Data Science Journey 🚀

This repository documents my intensive bootcamp journey transitioning from **Industrial Engineering** to **Data Science**. It contains coding exercises, algorithms implemented from scratch, and mini-projects focusing on the mathematical foundations of Machine Learning.

## 📂 Repository Structure

### 1. Pandas & Data Analysis (`/01_Pandas_Data_Analysis`)
**Objective:** Transitioning from spreadsheet-based logic to Pythonic data manipulation and vectorization.

- **`01_basic_production_metrics.py`**: 
  - Introduction to Pandas DataFrame structure.
  - Basic KPI calculation and manual data entry simulation.
- **`02_shift_performance_analysis.py`**: 
  - Loading external data (`.csv`) and handling file paths dynamically.
  - Comparative analysis of shift performance (Day vs. Night) using GroupBy.
- **`03_time_series_production_trends.py`**: 
  - Handling `Datetime` objects for time-series analysis.
  - Trend visualization and identifying top defect days using sorting algorithms.
- **`04_automated_production_report.py`**: 
  - **Automation:** Creating reusable functions to generate standardized reports for different factories.
  - demonstratiing modular coding practices.

### 2. Regression Models (`/02_Regression_Models`)
**Objective:** Mastering predictive analytics using Linear and Non-Linear algorithms.

- **`01_simple_linear_regression.py`**:
  - **Single Variable Analysis:** Predicting costs based on production volume.
  - **Machine Efficiency:** Analyzing depreciation trends (negative slope).
- **`02_multiple_linear_regression.py`**:
  - **Multivariable Analysis (Clean Room Case):** Predicting energy bills based on 3 variables (Production, Temperature, Machines).
  - Visualization of "Actual vs. Predicted" values to assess model performance.
- **`03_regression_model_evaluation.py`**:
  - **Model Validation:** Implementing Train-Test Split to prevent overfitting.
  - **Metrics:** Calculating MAE (Mean Absolute Error) and R² Score.
- **`04_decision_tree_regressor.py`**:
  - **Non-Linear Modeling:** Using Decision Trees for complex, rule-based datasets.
  - Visualizing the decision logic (Tree Diagram).

### 3. Classification Models (`/03_Classification_Models`)
- **Focus:** Predicting binary outcomes (0/1) using Logistic Regression.
- **Projects:**
  - **E-Commerce Purchase Prediction:** Analyzing customer behavior (Age, Duration) to predict purchase probability.
  - **Confusion Matrix Analysis:** Understanding the business cost of False Positives vs. False Negatives.

---

## 🛠 Tools & Technologies
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Environment:** VS Code

## 📢 Note on Datasets
Since the primary goal of this repository is to understand the **logic and mathematics** behind algorithms, simple and synthetic datasets (Small Data) are used intentionally. Real-world "Big Data" projects and Cloud deployments will be added in future modules.

---
*Author: Merve Kenc*
