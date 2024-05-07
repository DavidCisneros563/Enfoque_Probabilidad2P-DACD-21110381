#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Definir la función de activación de Heaviside
def heaviside(x):
    return np.where(x >= 0, 1, -1)

# Regla de aprendizaje de Hebb
def hebb_aprendizaje(X):
    num_muestras, num_caracteristicas = X.shape
    W = np.zeros((num_caracteristicas, num_caracteristicas))
    for i in range(num_muestras):
        W += np.outer(X[i], X[i])
    np.fill_diagonal(W, 0)
    return W / num_caracteristicas

# Regla de aprendizaje de Hamming
def hamming_aprendizaje(X):
    num_muestras, num_caracteristicas = X.shape
    W = np.zeros((num_caracteristicas, num_caracteristicas))
    for i in range(num_muestras):
        for j in range(num_caracteristicas):
            for k in range(j+1, num_caracteristicas):
                W[j, k] += X[i, j] * X[i, k]
                W[k, j] = W[j, k]
    return W / num_caracteristicas

# Regla de aprendizaje de Hopfield
def hopfield_aprendizaje(X):
    num_muestras, num_caracteristicas = X.shape
    W = np.zeros((num_caracteristicas, num_caracteristicas))
    for i in range(num_muestras):
        W += np.outer(X[i], X[i])
    np.fill_diagonal(W, 0)
    return W / num_caracteristicas

# Regla de aprendizaje de Boltzmann
def boltzmann_aprendizaje(X, temperatura=1.0, num_iteraciones=100):
    num_muestras, num_caracteristicas = X.shape
    W = np.zeros((num_caracteristicas, num_caracteristicas))
    for _ in range(num_iteraciones):
        for i in range(num_muestras):
            for j in range(num_caracteristicas):
                for k in range(j+1, num_caracteristicas):
                    W[j, k] += (X[i, j] * X[i, k]) / temperatura
                    W[k, j] = W[j, k]
        W *= (1.0 / num_muestras)
    return W

# Ejemplo de uso
X = np.array([[1, 1, -1, -1],
              [1, -1, 1, -1],
              [1, 1, 1, 1]])

print("Regla de aprendizaje de Hebb:")
print(hebb_aprendizaje(X))
print()

print("Regla de aprendizaje de Hamming:")
print(hamming_aprendizaje(X))
print()

print("Regla de aprendizaje de Hopfield:")
print(hopfield_aprendizaje(X))
print()

print("Regla de aprendizaje de Boltzmann:")
print(boltzmann_aprendizaje(X))