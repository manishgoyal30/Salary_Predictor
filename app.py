import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file_input']

    # Read in the CSV file
    data = pd.read_csv(file)
    input_data = np.asarray(data['YearsExperience']).reshape(-1, 1)

    # Make predictions for all the input data
    predictions = model.predict(input_data)

    # Combine the input data with the predictions and format the output
    output = []
    for i in range(len(data)):
        output.append([input_data[i][0], round(predictions[i], 2)])

    return render_template('index.html', prediction_data=output)

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "_main_":
    app.run(debug=True, port=5000)https://github.com/manishgoyal30/Salary_Predictor