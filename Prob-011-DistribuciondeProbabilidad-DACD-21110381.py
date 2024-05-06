#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Definir la distribución de probabilidad discreta
valores = np.array([1, 2, 3, 4, 5])
probabilidades = np.array([0.1, 0.2, 0.3, 0.2, 0.2])  # Suma de probabilidades debe ser 1

# Generar muestras aleatorias de la distribución de probabilidad
muestras_aleatorias = np.random.choice(valores, size=100, p=probabilidades)

# Calcular la media y la varianza de la distribución de probabilidad
media = np.sum(valores * probabilidades)
varianza = np.sum(probabilidades * (valores - media)**2)
print("Media de la distribución de probabilidad:", media)
print("Varianza de la distribución de probabilidad:", varianza)

# Imprimir las muestras aleatorias generadas
print("Muestras aleatorias generadas:", muestras_aleatorias)
