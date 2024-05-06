#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)  # Inicializar los pesos a cero (más uno para el sesgo)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Producto punto de los pesos y las entradas + sesgo
        activation = 1 if summation > 0 else 0  # Función de activación: escalón unitario
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs  # Actualizar los pesos
                self.weights[0] += self.learning_rate * (label - prediction)  # Actualizar el sesgo

# Ejemplo de uso
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_size=2)
perceptron.train(training_inputs, labels)

# Probando el perceptrón entrenado
inputs = np.array([1, 1])
print("Predicción para [1, 1]:", perceptron.predict(inputs))