import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("mlp_model.h5")

# Read the main CSV file
df_main = pd.read_csv("proteins_paac.csv")

# Select a random row from the dataframe
random_row = df_main.sample(n=1)

# Extract the features and prepare them for prediction
x_values = random_row.iloc[:, 2:].values  # Assuming id, seq are the first two columns
x_values = x_values.astype(np.float32)

# Make a prediction using the model
predicted_intensity = model.predict(x_values)

# Get the actual intensity values
spectrum_file = os.path.join("adjusted_spectra", f"{random_row['id'].values[0]}_em.csv")
df_spectrum = pd.read_csv(spectrum_file)
actual_intensity = df_spectrum["Intensity"].values

# Plotting actual vs. predicted values
plt.figure(figsize=(10, 6))
plt.plot(actual_intensity, label="Actual")
plt.plot(predicted_intensity[0], label="Predicted", linestyle="--")
plt.legend()
plt.title("Actual vs. Predicted Spectra")
plt.xlabel("Wavelength Index")
plt.ylabel("Intensity")
plt.show()

