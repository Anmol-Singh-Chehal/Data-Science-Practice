
def relu(x):
    if(x > 0):
        return x
    else:
        return 0

class Neuron:

    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs, activation):
        z = self.bias
        for i in range(len(inputs)):
            z += (inputs[i] * self.weights[i])
        z = activation(z)
        return z

n1 = Neuron([0.2, 0.5, -0.3], 0.1)
output = n1.forward([3, 2, 1], relu)
print("Output: ", output)

