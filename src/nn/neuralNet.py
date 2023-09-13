import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read the CSV file
data = pd.read_csv('emission.csv')
output = pd.read_csv('molecules.csv')

# Extract features (descriptors) and target (Emission max)
X = data.iloc[:, 1:]  # Exclude the first column (assuming it contains the SMILES)
y = output['Emission max (nm)']
y = np.array(y)  # Convert to numpy array for better handling

# Create a mask to filter out NaN values
mask = ~np.isnan(y)

# Apply the mask to exclude NaN values
y = y[mask]

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
model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
mse = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on test set:", mse)

# Predict on new data
new_data = pd.read_csv('molecules.csv')  # Replace with the new data
X_new = new_data.iloc[:, 1:]  # Exclude the first column (assuming it contains the SMILES)
X_new_scaled = scaler.transform(X_new)
predictions = model.predict(X_new_scaled)

# Save the model
model.save('model.h5')
