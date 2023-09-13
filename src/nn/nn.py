import numpy as np
import pandas as pd

# Activation functions and their derivatives

# Define the sigmoid activation function
def sigmoid(x):
    # Sigmoid function formula
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function for backpropagation
def sigmoid_derivative(x):
    s = sigmoid(x)
    # Derivative of sigmoid formula
    return s * (1 - s)

# Define the ReLU activation function
def relu(x):
    # ReLU function formula
    return np.maximum(0, x)

# Define the derivative of the ReLU function for backpropagation
def relu_derivative(x):
    # If x is greater than 0, return 1, otherwise return 0
    return np.where(x > 0, 1, 0)

# Define a class for each layer in the neural network
class Layer:
    def __init__(self, input_size, output_size, activation='relu'):
        # Initialize weights randomly with a small value
        self.weights = np.random.randn(input_size, output_size) * 0.01
        # Initialize biases to zeros
        self.biases = np.zeros((1, output_size))
        # To store the input for backpropagation
        self.input = None
        # To store the gradients of weights and biases for backpropagation
        self.dweights = None
        self.dbiases = None

        # Choose activation function based on the provided argument
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_derivative = sigmoid_derivative
        elif activation == 'relu':
            self.activation = relu
            self.activation_derivative = relu_derivative
        else:
            # Raise an error if the provided activation function is not supported
            raise ValueError(f"Unsupported activation function: {activation}")

    # Forward pass: compute the output of this layer given an input
    def forward(self, x):
        self.input = x
        # Multiply the input with the weights, add the biases, and pass it through the activation function
        return self.activation(np.dot(x, self.weights) + self.biases)

    # Backward pass: compute the gradients based on the output error
    def backward(self, dvalues):
        # Compute the gradient of the activation function
        dvalues = dvalues * self.activation_derivative(np.dot(self.input, self.weights) + self.biases)
        # Gradient for the weights
        self.dweights = np.dot(self.input.T, dvalues)
        # Gradient for the biases
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        # Return the gradient of the input to propagate the error to the previous layer
        return np.dot(dvalues, self.weights.T)

# Define the main neural network class
class NeuralNetwork:
    def __init__(self):
        # List to store all the layers in the network
        self.layers = []

    # Method to add a layer to the network
    def add(self, layer):
        self.layers.append(layer)

    # Forward pass through all the layers to compute the network's output
    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    # Training method
    def train(self, x, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Compute the output for the current input
            outputs = self.predict(x)
            # Compute the mean squared error
            loss = ((outputs - y) ** 2).mean()
            print(f'Epoch {epoch + 1}, Loss: {loss:.4f}')
            # Compute the gradient of the loss with respect to the output
            dvalues = 2 * (outputs - y) / outputs.shape[0]
            # Backpropagate the error through all the layers
            for layer in reversed(self.layers):
                dvalues = layer.backward(dvalues)
                # Update the weights and biases using the gradients
                layer.weights -= learning_rate * layer.dweights
                layer.biases -= learning_rate * layer.dbiases

    # Test the trained model on a single input
    def test(self, x):
        outputs = self.predict(x)
        print(f'results: {outputs}')

# Sample data
#df = pd.read_csv('train_nonnan.csv')
#y = df['Emission max (nm)'].values.reshape(-1, 1)
#x = df.drop(columns=['Emission max (nm)', 'Tag', 'Name']).values
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
# Define and train the neural network
model = NeuralNetwork()
model.add(Layer(2, 512, activation='sigmoid'))
model.add(Layer(512, 256, activation='sigmoid'))
model.add(Layer(256, 128, activation='sigmoid'))
model.add(Layer(128, 1, activation='sigmoid'))  # linear output

model.train(x, y, epochs=1000, learning_rate=0.01)
model.test([0,0])
model.test([1,0])
model.test([0,1])
model.test([1,1])
print("done")
