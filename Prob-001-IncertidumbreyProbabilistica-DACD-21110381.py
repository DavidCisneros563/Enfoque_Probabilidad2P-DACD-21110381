#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Definir una distribución de probabilidad
probabilidades = np.array([0.2, 0.3, 0.5])  # Por ejemplo, tres eventos con estas probabilidades

# Muestra aleatoria según la distribución de probabilidad
muestra = np.random.choice([0, 1, 2], p=probabilidades)
print("Muestra aleatoria:", muestra)

# Calcular la media y la varianza de la distribución
media = np.mean(probabilidades)
varianza = np.var(probabilidades)
print("Media de la distribución:", media)
print("Varianza de la distribución:", varianza)
