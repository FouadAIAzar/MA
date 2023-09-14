# README: Deep Learning Model for Predicting Emission Max

This script is designed to:
1. Read data from a CSV file
2. Prepare the data for training
3. Create, compile, train, and evaluate a neural network model
4. Predict on new data
5. Visualize the model's predictions
6. Save the model for future use.

## Prerequisites:

- pandas
- numpy
- tensorflow
- sklearn
- matplotlib

Ensure you have the aforementioned libraries installed using `pip install`.

## Detailed Breakdown:

### 1. Imports

```python
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

- `pandas` and `numpy` are for data manipulation.
- `tensorflow` is for building and training the neural network.
- `train_test_split` is to split data into training and testing subsets.
- `StandardScaler` standardizes the features by removing the mean and scaling to unit variance.
- `matplotlib` for plotting and visualization.

### 2. Data Loading

```python
data = pd.read_csv('train.csv')
```
- Reads a CSV file named 'train.csv' and stores it in a DataFrame called 'data'.

### 3. Data Preparation

```python
X = data.drop(columns=['Tag', 'Name', 'Emission max (nm)'])
y = data['Emission max (nm)']
y = np.array(y)
```
- Features `X` are extracted by dropping columns 'Tag', 'Name', and 'Emission max (nm)'.
- The target `y` is the 'Emission max (nm)' column, converted to a numpy array for better compatibility with TensorFlow.

### 4. Data Splitting

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- Data is split into training and testing sets with 80% for training and 20% for testing.

### 5. Feature Scaling

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
- A standard scaler is used to normalize features, ensuring that all features are on a similar scale.

### 6. Neural Network Creation

```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1)
])
```
- A sequential model with two hidden layers of 128 neurons each is built.
- The activation function for hidden layers is 'ReLU'.
- The output layer has one neuron with a linear activation function.

### 7. Model Compilation

```python
model.compile(loss='mean_squared_error', optimizer='adam')
```
- The model uses the mean squared error loss function and the Adam optimizer.

### 8. Model Training

```python
model.fit(X_train_scaled, y_train, epochs=10000, batch_size=32, validation_split=0.2)
```
- The model is trained for 10,000 epochs with a batch size of 32.
- 20% of the training data is used as a validation set.

### 9. Model Evaluation

```python
mse = model.evaluate(X_test_scaled, y_test)
print("Mean Squared Error on test set:", mse)
```
- The model's performance is evaluated on the test set and the Mean Squared Error (MSE) is printed.

### 10. Predictions

```python
new_data = pd.read_csv('train.csv')
X_new = new_data.drop(columns=['Tag', 'Name', 'Emission max (nm)'])
X_new_scaled = scaler.transform(X_new)
predicted = model.predict(X_new_scaled)
```
- A new dataset (in this script it's the same 'train.csv') is loaded.
- Features are extracted, scaled, and predictions are made using the trained model.

### 11. Visualization

```python
plt.scatter(y_test, y_pred)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Actual vs Predicted values')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')
plt.show()
```
- A scatter plot is drawn comparing actual vs. predicted values.
- A red line representing y=x is drawn to visually compare predictions against actual values.

### 12. Model Saving

```python
model.save('model.h5')
```
- The trained model is saved in the H5 format with the filename 'model.h5'.

**Note:** Before using this script on new data, ensure that the data has the same structure and columns as 'train.csv' and preprocess it similarly.
