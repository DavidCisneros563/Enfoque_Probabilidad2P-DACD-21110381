#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generar datos de ejemplo
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# Clasificación con k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predecir el grupo al que pertenecen nuevos puntos
nuevos_puntos = np.array([[0, 2], [3, 2.5], [0, 4]])
predicciones_knn = knn.predict(nuevos_puntos)

# Agrupamiento con k-Means
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# Obtener los centroides de los clusters
centroides = kmeans.cluster_centers_

# Predecir los clusters de los puntos de ejemplo
predicciones_kmeans = kmeans.predict(X)

# Visualizar los resultados
plt.figure(figsize=(15, 6))

# Graficar datos de ejemplo con colores verdaderos
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', s=50)
plt.title("Datos de ejemplo con colores verdaderos")

# Graficar datos de ejemplo con colores predichos por k-NN
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=predicciones_knn, cmap='viridis', s=50)
plt.scatter(nuevos_puntos[:, 0], nuevos_puntos[:, 1], c='red', marker='x', s=100)
plt.title("Clasificación con k-NN")

plt.show()

# Visualizar los centroides y los clusters predichos por k-Means
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=predicciones_kmeans, cmap='viridis', s=50)
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='x', s=200)
plt.title("Agrupamiento con k-Means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.grid(True)
plt.show()
