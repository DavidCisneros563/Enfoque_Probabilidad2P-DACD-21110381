#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class Perceptron:
    def __init__(self, num_entradas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.random.rand(num_entradas + 1)  # +1 para el peso del sesgo
    
    def funcion_activacion(self, entrada):
        return 1 if entrada >= 0 else 0
    
    def predict(self, entrada):
        suma_ponderada = np.dot(entrada, self.pesos[1:]) + self.pesos[0]  # Producto punto + sesgo
        return self.funcion_activacion(suma_ponderada)
    
    def fit(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                prediccion = self.predict(entrada)
                error = etiqueta - prediccion
                self.pesos[1:] += self.tasa_aprendizaje * error * entrada
                self.pesos[0] += self.tasa_aprendizaje * error

class Adaline:
    def __init__(self, num_entradas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.random.rand(num_entradas + 1)  # +1 para el peso del sesgo
    
    def funcion_activacion(self, entrada):
        return entrada
    
    def predict(self, entrada):
        suma_ponderada = np.dot(entrada, self.pesos[1:]) + self.pesos[0]  # Producto punto + sesgo
        return self.funcion_activacion(suma_ponderada)
    
    def fit(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                prediccion = self.predict(entrada)
                error = etiqueta - prediccion
                self.pesos[1:] += self.tasa_aprendizaje * error * entrada
                self.pesos[0] += self.tasa_aprendizaje * error

class Madaline:
    def __init__(self, num_entradas, num_salidas, tasa_aprendizaje=0.1, epocas=100):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.random.rand(num_entradas + 1, num_salidas)  # +1 para el peso del sesgo
    
    def funcion_activacion(self, entrada):
        return entrada
    
    def predict(self, entrada):
        suma_ponderada = np.dot(entrada, self.pesos[1:]) + self.pesos[0]  # Producto punto + sesgo
        return self.funcion_activacion(suma_ponderada)
    
    def fit(self, X, y):
        for _ in range(self.epocas):
            for entrada, etiqueta in zip(X, y):
                prediccion = self.predict(entrada)
                error = etiqueta - prediccion
                self.pesos[1:] += self.tasa_aprendizaje * error * entrada[:, np.newaxis]  # Añadir dimensión para broadcasting
                self.pesos[0] += self.tasa_aprendizaje * error

# Ejemplo de uso para el Perceptrón
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

perceptron = Perceptron(num_entradas=2)
perceptron.fit(X, y)
print("Perceptron - Predicciones:", [perceptron.predict(entrada) for entrada in X])

# Ejemplo de uso para ADALINE
adaline = Adaline(num_entradas=2)
adaline.fit(X, y)
print("ADALINE - Predicciones:", [adaline.predict(entrada) for entrada in X])

# Ejemplo de uso para MADALINE
madaline = Madaline(num_entradas=2, num_salidas=1)
madaline.fit(X, y)
print("MADALINE - Predicciones:", [madaline.predict(entrada) for entrada in X])