import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model
model = load_model('model.h5')

# Load the data from train.csv
data = pd.read_csv('train.csv')

# Extract the input features and the output label
X = data.drop(columns=['Tag', 'Name', 'Emission max (nm)'])
y = data['Emission max (nm)']

# Scale the X data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Evaluate the model using the scaled data
evaluation = model.evaluate(X_scaled, y)
if isinstance(evaluation, list):
    loss = evaluation[0]
    accuracy = evaluation[1]
    print(f'Loss: {loss}')
    print(f'Accuracy: {accuracy}')
else:
    loss = evaluation
    print(f'Loss: {loss}')

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

