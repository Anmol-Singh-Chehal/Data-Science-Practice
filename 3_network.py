
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

class layer:
    def __init__(self, Neurons):
        self.Neurons = Neurons

    def forward(self, inputs, activation):
        output = []
        for Neuron in self.Neurons:
            z = Neuron.forward(inputs)
            z = activation(z)
            output.append(z)

        return output

class Network:
    def __init__(self, layers):
        self.layers = layers

    def forward(self, inputs, activation):
        outputs = inputs
        for layer in self.layers:
            outputs = layer.forward(outputs, activation)

        return outputs


layer1 = layer([
    Neuron([0.2, 0.5, -0.3], 0.1),
    Neuron([-0.4, 0.7, 0.2], -0.2),
    Neuron([0.6, -0.1, 0.8], 0.3)
])

layer2 = layer([
    Neuron([0.4, -0.2, 0.5], 0.1),
    Neuron([-0.3, 0.8, 0.2], -0.1)
])

network1 = Network([layer1, layer2])
output = network1.forward([3, 2, 1], relu)
print("Output: ", output)