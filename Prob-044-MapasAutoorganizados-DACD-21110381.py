#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

# Generar datos de ejemplo
np.random.seed(0)
data = np.random.rand(100, 2)

# Definir las dimensiones del mapa SOM
som_shape = (10, 10)

# Inicializar el mapa SOM
som = MiniSom(som_shape[0], som_shape[1], 2, sigma=0.5, learning_rate=0.5)

# Inicializar los pesos del mapa SOM con datos aleatorios
som.random_weights_init(data)

# Entrenar el mapa SOM
som.train_batch(data, 1000)

# Obtener las coordenadas de los nodos ganadores para cada muestra
winners = np.array([som.winner(x) for x in data])

# Graficar el mapa SOM y las muestras
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Graficar el mapa de distancias
plt.colorbar()

# Graficar las muestras en el mapa SOM
for i, j in zip(*winners.T):
    plt.text(i + 0.5, j + 0.5, 'x', ha='center', va='center', color='r', fontsize=12)

plt.title('Mapa Autoorganizado de Kohonen')
plt.show()
