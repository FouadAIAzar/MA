import numpy as np

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Layer class
class Layer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))
        self.input = None
        self.dweights = None
        self.dbiases = None

    def forward(self, x):
        self.input = x
        return np.dot(x, self.weights) + self.biases

    def backward(self, dvalues):
        self.dweights = np.dot(self.input.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        return np.dot(dvalues, self.weights.T)

# Neural network class
class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def predict(self, x):
        for layer in self.layers:
            x = sigmoid(layer.forward(x))
        return x

    def train(self, x, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Feedforward
            outputs = self.predict(x)

            # Calculate Loss (Mean Squared Error)
            loss = ((outputs - y) ** 2).mean()
            print(f'Epoch {epoch + 1}, Loss: {loss:.4f}')

            # Backpropagation
            dvalues = 2 * (outputs - y) / outputs.shape[0] * sigmoid_derivative(outputs)
            for layer in reversed(self.layers):
                dvalues = layer.backward(dvalues)

                # Update parameters
                layer.weights -= learning_rate * layer.dweights
                layer.biases -= learning_rate * layer.dbiases

# Sample data
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Model definition and training
model = NeuralNetwork()
model.add(Layer(2, 5))
model.add(Layer(5, 1))

model.train(x, y, epochs=100000, learning_rate=5.0)

print("done")