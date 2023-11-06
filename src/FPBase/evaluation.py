import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("mlp_model.h5")

# Read the main CSV file
df_main = pd.read_csv("proteins_paac.csv")

# Create the figures directory if it doesn't exist
if not os.path.exists("figures"):
    os.makedirs("figures")

# Iterate over all rows in the dataframe
for index, row in df_main.iterrows():

    # Extract the features and prepare them for prediction
    x_values = row[2:].values.reshape(1, -1)  # Assuming id, seq are the first two columns and reshape to match the model input shape
    x_values = x_values.astype(np.float32)

    # Make a prediction using the model
    predicted_intensity = model.predict(x_values)

    # Get the actual intensity values
    spectrum_file = os.path.join("adjusted_spectra", f"{row['id']}_em.csv")
    df_spectrum = pd.read_csv(spectrum_file)
    actual_intensity = df_spectrum["Intensity"].values

    # Plotting actual vs. predicted values
    plt.figure(figsize=(10, 6))
    plt.plot(actual_intensity, label="Actual")
    plt.plot(predicted_intensity[0], label="Predicted", linestyle="--")
    plt.legend()
    plt.title(f"Actual vs. Predicted Spectra for ID {row['id']}")
    plt.xlabel("Wavelength Index")
    plt.ylabel("Intensity")

    # Save the figure
    plt.savefig(os.path.join("figures", f"{row['id']}_comparison.png"))
    plt.close()  # Close the current figure to free up memory

