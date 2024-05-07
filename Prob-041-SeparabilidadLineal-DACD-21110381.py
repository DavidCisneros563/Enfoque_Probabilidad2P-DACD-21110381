#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo separables linealmente
np.random.seed(0)
num_muestras = 100
X1 = np.random.randn(num_muestras, 2) + np.array([2, 2])  # Clase 1
X2 = np.random.randn(num_muestras, 2) + np.array([-2, -2])  # Clase 2

# Visualizar los datos generados
plt.figure(figsize=(8, 6))
plt.scatter(X1[:, 0], X1[:, 1], color='blue', label='Clase 1')
plt.scatter(X2[:, 0], X2[:, 1], color='red', label='Clase 2')
plt.title('Datos Separables Linealmente')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.legend()
plt.grid(True)
plt.show()
