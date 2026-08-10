class Neuron:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        z = self.bias
        for i in range(len(inputs)):
            z += (inputs[i] * self.weights[i])

        return z

def relu(x):
    if x > 0:
        return x
    else:
        return 0

class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, inputs, activation):
        output = []
        for neuron in self.neurons:
            z = neuron.forward(inputs)
            z = activation(z)
            output.append(z)

        return output

layer1 = Layer([
    Neuron([0.2, 0.5, -0.3], 0.1),
    Neuron([-0.4, 0.7, 0.2], -0.2),
    Neuron([0.6, -0.1, 0.8], 0.3)
])
output = layer1.forward([3, 2, 1], relu)
print("Output: ", output)