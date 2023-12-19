import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Ask the user to enter the folder path
folder_path = input("Please enter the folder path: ")

# Construct the model file path
model_path = os.path.join(folder_path, "model.h5")

try:
    # Load the pre-trained model
    model = load_model(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Construct the test file path
test_file_path = os.path.join(folder_path, "test.csv")

try:
    # Load the data from test.csv
    data = pd.read_csv(test_file_path)
except FileNotFoundError:
    print("The file 'test.csv' was not found.")
    exit()

# Extract the input features and the output label
X = data.drop(columns=['Tag', 'Name', 'Emission max (nm)'])
y = data['Emission max (nm)']

# Scale the X data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Evaluate the model using the scaled data
try:
    evaluation = model.evaluate(X_scaled, y)
    if isinstance(evaluation, list):
        loss = evaluation[0]
        accuracy = evaluation[1]
        print(f'Loss: {loss}')
        print(f'Accuracy: {accuracy}')
    else:
        loss = evaluation
        print(f'Loss: {loss}')
except Exception as e:
    print(f"Error during model evaluation: {e}")

# Predict using the model on scaled data
y_pred = model.predict(X_scaled)

# Calculate mean absolute error
mae = mean_absolute_error(y, y_pred)
print(f'Mean Absolute Error: {mae}')

# Write performance information to a text file
performance_file_path = os.path.join(folder_path, 'performance.txt')
with open(performance_file_path, 'w') as file:
    file.write(f'Loss: {loss}\n')
    file.write(f'Mean Absolute Error: {mae}\n')

# Plot actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, alpha=0.5)
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red')  
plt.savefig(os.path.join(folder_path, 'actual_vs_predicted.png'))  
plt.close()

# Histogram of residuals
residuals = y - y_pred.reshape(-1)
plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=50, alpha=0.75)
plt.title('Histogram of Residuals')
plt.xlabel('Residual Value')
plt.ylabel('Frequency')
plt.savefig(os.path.join(folder_path, 'residuals_histogram.png')) 
plt.close()
