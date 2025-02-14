from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model, scaler, and feature names
model = joblib.load('fraud_detection_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_names = joblib.load('feature_names.pkl')  # Load feature names

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML frontend

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        data = request.form.to_dict()

        # Convert input to a DataFrame
        input_data = pd.DataFrame([data])

        # Ensure the input data has the same columns as the training data
        input_data = pd.get_dummies(input_data, drop_first=True)
        input_data = input_data.reindex(columns=feature_names, fill_value=0)

        # Scale the input data
        input_scaled = scaler.transform(input_data)

        # Make a prediction
        prediction = model.predict(input_scaled)

        # Return the result
        result = "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)