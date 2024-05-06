#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# Visualizar los datos de ejemplo
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], s=50, cmap='viridis')
plt.title("Datos de ejemplo")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.grid(True)
plt.show()

# Aplicar el algoritmo K-Means para agrupar los datos
k = 4  # Número de clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)

# Obtener los centroides y las etiquetas de los clusters
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

# Visualizar los clusters junto con los centroides
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, s=50, cmap='viridis', alpha=0.7)
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, marker='X')
plt.title("Agrupamiento con K-Means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.grid(True)
plt.show()
