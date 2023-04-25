# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

salary_data = pd.read_csv('G:\Third Year\SEM-6\ML\LAB\Project_Flask\Salary_Data.csv')

X = salary_data['YearsExperience']
Y = salary_data['Salary']
X = np.asarray(X)
X = X.reshape(-1, 1)
Y = np.asarray(Y)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, Y_train)

# Saving model to disk
pickle.dump(model, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))

# Predicting the output for a single input


# Predicting the output for a single input
input_data = np.array([2]) # convert the input to a numpy array
input_data = input_data.reshape(-1, 1) # reshape the input to a 2D array
prediction = model.predict(input_data)
print(prediction)