#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class Neurona:
    def __init__(self, num_entradas):
        self.pesos = np.random.rand(num_entradas)  # Inicializar pesos aleatorios
        self.umbral = np.random.rand()  # Inicializar umbral aleatorio

    def activacion(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos) - self.umbral
        return 1 if suma_ponderada >= 0 else 0

# Ejemplo de uso
neurona = Neurona(num_entradas=2)
entradas = np.array([1, 0.5])  # Ejemplo de entradas
resultado = neurona.activacion(entradas)
print("Resultado de la neurona:", resultado)
