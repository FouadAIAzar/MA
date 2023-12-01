import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

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

    # Normalize the predicted intensity between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_predicted_intensity = scaler.fit_transform(predicted_intensity.reshape(-1, 1)).reshape(-1)

    # Get the actual intensity values
    spectrum_file = os.path.join("adjusted_spectra", f"{row['id']}_em.csv")
    df_spectrum = pd.read_csv(spectrum_file)
    actual_intensity = df_spectrum["Intensity"].values

    # Plotting actual vs. normalized predicted values
    plt.figure(figsize=(10, 6))
    plt.plot(actual_intensity, label="Actual")
    plt.plot(normalized_predicted_intensity, label="Normalized Predicted", linestyle="--")
    plt.legend()
    plt.title(f"Actual vs. Normalized Predicted Spectra for ID {row['id']}")
    plt.xlabel("Wavelength Index")
    plt.ylabel("Intensity")

    # Save the figure
    plt.savefig(os.path.join("figures", f"{row['id']}_comparison.png"))
    plt.close()  # Close the current figure to free up memory

