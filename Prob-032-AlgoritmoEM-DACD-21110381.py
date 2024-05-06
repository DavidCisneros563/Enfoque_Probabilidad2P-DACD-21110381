#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos de ejemplo con tres grupos (clusters)
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Inicializar el modelo de mezcla de gaussianas
modelo = GaussianMixture(n_components=3, random_state=42)

# Entrenar el modelo con los datos de ejemplo
modelo.fit(X)

# Mostrar los parámetros iniciales del modelo
print("Parámetros iniciales:")
print("Pesos de los componentes:", modelo.weights_)
print("Medias de los componentes:", modelo.means_)
print("Matrices de covarianza de los componentes:", modelo.covariances_)

# Realizar el algoritmo EM para actualizar los parámetros del modelo
modelo.fit(X)

# Mostrar los parámetros actualizados del modelo
print("\nParámetros actualizados después de una iteración del algoritmo EM:")
print("Pesos de los componentes:", modelo.weights_)
print("Medias de los componentes:", modelo.means_)
print("Matrices de covarianza de los componentes:", modelo.covariances_)