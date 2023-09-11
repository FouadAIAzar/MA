import numpy as np

# Activation functions and their derivatives
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

class Layer:
    def __init__(self, input_size, output_size, activation='relu'):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))
        self.input = None
        self.dweights = None
        self.dbiases = None

        # Choose activation function
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_derivative = sigmoid_derivative
        elif activation == 'relu':
            self.activation = relu
            self.activation_derivative = relu_derivative
        else:
            raise ValueError(f"Unsupported activation function: {activation}")

    def forward(self, x):
        self.input = x
        return self.activation(np.dot(x, self.weights) + self.biases)

    def backward(self, dvalues):
        dvalues = dvalues * self.activation_derivative(np.dot(self.input, self.weights) + self.biases)
        self.dweights = np.dot(self.input.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        return np.dot(dvalues, self.weights.T)

class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def train(self, x, y, epochs, learning_rate):
        for epoch in range(epochs):
            outputs = self.predict(x)
            loss = ((outputs - y) ** 2).mean()
            print(f'Epoch {epoch + 1}, Loss: {loss:.4f}')

            dvalues = 2 * (outputs - y) / outputs.shape[0]
            for layer in reversed(self.layers):
                dvalues = layer.backward(dvalues)
                layer.weights -= learning_rate * layer.dweights
                layer.biases -= learning_rate * layer.dbiases

# Sample data
x = np.random.randn(100, 1877)
y = np.random.randn(100, 1)

# Define and train the neural network
model = NeuralNetwork()
model.add(Layer(1877, 512, activation='relu'))
model.add(Layer(512, 256, activation='sigmoid'))
model.add(Layer(256, 128, activation='relu'))
model.add(Layer(128, 1, activation='relu'))  # linear output

model.train(x, y, epochs=1000, learning_rate=0.01)

print("done")

