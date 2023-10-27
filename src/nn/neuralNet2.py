import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('train.csv')

# Extract features (descriptors) and target (Emission max)
X = data.drop(columns=['Tag', 'Name', 'Emission max (nm)'])
y = data['Emission max (nm)']
y = np.array(y)  # Convert to numpy array for better handling

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the neural network model with Dropout layers
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(939, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(470, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Implement Early Stopping
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50, restore_best_weights=True)

# Train the model with validation split and early stopping
model.fit(X_train_scaled, y_train, epochs=1000, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

# Evaluate the model on the test set
mse = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on test set:", mse)

# Save the model
model.save('model.h5')

# If you have new data, predict using it
# For demonstration purposes, I'm skipping this part

# Predict on test data (for visualization)
y_pred = model.predict(X_test_scaled)

# Plot actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Actual vs Predicted values [Emission]')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # y=x line
plt.show()

