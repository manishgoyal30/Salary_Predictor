# Salary_Predictor

# Description
we have already a train model, which predicts salary when user give input about their expeience, then we create pickle file from that model. then we create the html and css for the webpage creation, and there user can upload the file in csv format, and get the predicted salary as we created the app.py to take the inputs from the uploaded file'

# Dependencies must be install
To run the project, you need to install the necessary dependencies listed here:
numpy 
pandas
Flask, 
request, 
jsonify,
pickle

# Once the dependencies are installed, you can start the Flask application by running:
python app.py
or
flask run

This will start the Flask application on http://localhost:5000/.


# Usage
Once the Flask application is running, you can access the home page by visiting http://localhost:5000/. Here, you can upload a CSV file containing years of experience data and get predictions for the corresponding salaries.

You can also use the /predict_api endpoint to get predictions programmatically. Send a POST request to http://localhost:5000/predict_api with a JSON payload containing the years of experience data. The endpoint will return a JSON response containing the predicted salaries.

# Model
The machine learning model used in this project is a simple linear regression model that predicts salaries based on years of experience. The model is trained on the Salary_Data.csv dataset, which contains salaries and corresponding years of experience for a set of employees.

The model is saved as a pickle file model.pkl and loaded into memory when the Flask application starts.

# Github Link:
https://github.com/manishgoyal30/Salary_Predictor