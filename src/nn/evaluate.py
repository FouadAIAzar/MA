import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
# from tensorflow.keras.utils import plot_model  # Uncomment if you want to plot the model structure

# Ask the user to enter the model file path
model_path = input("Please enter the model file path you want to evaluate: ")

try:
    # Load the pre-trained model
    model = load_model(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

try:
    # Load the data from test.csv
    data = pd.read_csv('test.csv')
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

# Plot actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, alpha=0.5)
plt.title('Actual vs. Predicted Values')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red')  # Diagonal line
plt.show()

# Histogram of residuals
residuals = y - y_pred.reshape(-1)
plt.figure(figsize=(10, 6))
plt.hist(residuals, bins=50, alpha=0.75)
plt.title('Histogram of Residuals')
plt.xlabel('Residual Value')
plt.ylabel('Frequency')
plt.show()

