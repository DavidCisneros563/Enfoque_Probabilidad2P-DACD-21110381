#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial


import numpy as np

# Definir la distribución conjunta de probabilidades P(X, Y)
# Supongamos que tenemos 3 valores posibles para X y 2 valores posibles para Y
distribucion_conjunta = np.array([[0.1, 0.2],
                                  [0.3, 0.15],
                                  [0.2, 0.25]])

# Calcular la probabilidad condicionada P(Y|X=x) para X=x_1 (por ejemplo, x_1=0)
x_index = 0
x_value = distribucion_conjunta[x_index]
probabilidad_condicionada = x_value / np.sum(x_value)
print("Probabilidad condicionada P(Y|X=x_1):", probabilidad_condicionada)

# Normalizar las probabilidades condicionadas
probabilidad_condicionada_normalizada = probabilidad_condicionada / np.sum(probabilidad_condicionada)
print("Probabilidad condicionada normalizada:", probabilidad_condicionada_normalizada)