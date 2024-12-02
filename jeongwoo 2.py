inputs = [1.0, 2.0 , 3.0 , 0.6]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

import random

def init_weights(inputs):
    return [random.uniform(-1,1) for i in inputs]

def cal(inputs, weights, bias):
    output = []
    output = []
    output = []
    output = []
    output = []
    return output


def cal_neuron(num_neuron,inputs):
    output = []
    for i in range(num_neuron):
        weights = init_weights(len(inputs))
        bias = random.uniform(-1,1)
        output = cal(inputs, weights , bias)
        output.append(output)
    return output
