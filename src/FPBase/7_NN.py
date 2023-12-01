import pandas as pd
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping

# 1. Data Preprocessing

# Read the main CSV file
df_main = pd.read_csv("proteins_paac.csv")

X = []
Y = []

for index, row in df_main.iterrows():
    # Extracting ID and reading corresponding CSV
    spectrum_file = os.path.join("adjusted_spectra", f"{row['id']}_em.csv")
    df_spectrum = pd.read_csv(spectrum_file)
    
    # Extracting intensity values
    intensity_values = df_spectrum["Intensity"].values
    
    # Extracting the rest of the values from main CSV
    x_values = row[2:].values  # Assuming id, seq are the first two columns
    
    X.append(x_values)
    Y.append(intensity_values)

X = np.array(X)
Y = np.array(Y)

X = X.astype(np.float32)
Y = Y.astype(np.float32)


# 2. Model Building

# MLP architecture
model = Sequential()
model.add(Dense(128, input_dim=X.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(Y.shape[1], activation='linear'))

model.compile(optimizer='adam', loss='mean_squared_error')

# 3. Model Training

# Define Early Stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Training the model with Early Stopping
model.fit(X, Y, epochs=1000, batch_size=32, validation_split=0.2, callbacks=[early_stopping])

# Save the model
model.save("mlp_model.h5")

# 4. Model Evaluation

# Predict the Y values on the validation set
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42)
Y_pred = model.predict(X_val)

# Calculate the MSE
mse = tf.keras.losses.MeanSquaredError()
mse_val = mse(Y_val, Y_pred).numpy()

print(f"Validation MSE: {mse_val}")

# Optionally, if you want to compute other metrics:
mae = tf.keras.losses.MeanAbsoluteError()
mae_val = mae(Y_val, Y_pred).numpy()

print(f"Validation MAE: {mae_val}")

# R-squared is not directly available in Keras, but can be computed using sklearn
from sklearn.metrics import r2_score
r2_val = r2_score(Y_val, Y_pred)
print(f"Validation R^2: {r2_val}")

