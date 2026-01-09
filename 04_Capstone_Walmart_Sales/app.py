import joblib
import pandas as pd
from flask import Flask, request, jsonify
from pathlib import Path

"""
Walmart Sales Prediction API
----------------------------
This script initializes a Flask web server to serve the trained Random Forest model.
It handles:
1. Model Loading
2. Request Processing
3. Feature Alignment
4. Prediction & Response
"""

app = Flask(__name__)

# --- LOAD MODEL ---
current_dir = Path(__file__).parent
model_path = current_dir / "random_forest_model.pkl"

print(f"Loading model from: {model_path} ...")

try:
    model = joblib.load(model_path)
    print("Model Loaded Successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- PREDICTION ENDPOINT ---
@app.route('/predict', methods=['POST'])
def predict():
    # Ensure model is loaded
    if not model:
        return jsonify({'status': 'error', 'message': 'Model could not be loaded.'})

    try:
        # Get Data
        data = request.get_json()
        input_df = pd.DataFrame([data])
        
        # --- ROBUST FEATURE ALIGNMENT ---
        # Ensure input features match the training features exactly
        
        # Get the feature names expected by the model
        expected_cols = model.feature_names_in_
        
        # Add missing columns with 0
        for col in expected_cols:
            if col not in input_df.columns:
                input_df[col] = 0
                
        # Reorder columns to match training order & drop unexpected columns
        input_df = input_df[expected_cols]
        
        # -----------------------------------------------

        # Make Prediction
        prediction = model.predict(input_df)[0]
        
        # Return Response
        return jsonify({
            'status': 'success',
            'predicted_sales': round(prediction, 2),
            'currency': 'USD'
        })
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# --- RUN SERVER ---
if __name__ == '__main__':
    # debug=True allows auto-restart on code changes. 
    # Disable this in a real production environment.
    app.run(debug=True)