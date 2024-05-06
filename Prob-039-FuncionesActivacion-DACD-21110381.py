#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

# Ejemplo de uso
x = np.array([-1, 0, 1])
print("Función Sigmoid:", sigmoid(x))
print("Función ReLU:", relu(x))
print("Función Tangente Hiperbólica:", tanh(x))
print("Función Softmax:", softmax(x))
