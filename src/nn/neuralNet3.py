import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('train_absorption.csv')
# Extract features (descriptors) and target (Emission max)
X = data.drop(columns=['Tag', 'Name', 'Absorption max (nm)'])
y = data['Absorption max (nm)']
y = np.array(y)  # Convert to numpy array for better handling

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer with no activation (linear activation)
])

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train_scaled, y_train, epochs=1000, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
mse = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on test set:", mse)

# Predict on new data (if needed)
# Here, I'm keeping this part from the original code but be aware you'll likely need to preprocess the new data similarly to how you preprocessed 'train.csv'
new_data = pd.read_csv('train_absorption.csv')
X_new = new_data.drop(columns=['Tag', 'Name', 'Absorption max (nm)'])
X_new_scaled = scaler.transform(X_new)
predicted = model.predict(X_new_scaled)

y_test = y
y_pred = predicted

# Plot actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Actual vs Predicted values [Emission]')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # y=x line
plt.show()

# Save the model
model.save('model_absorption.h5')

