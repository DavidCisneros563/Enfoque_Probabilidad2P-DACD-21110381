#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
from hmmlearn import hmm

# Definir el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)

# Matriz de probabilidad de transición de estado
modelo_hmm.transmat_ = np.array([[0.7, 0.3],  # Probabilidades de transición del estado 0
                                 [0.4, 0.6]]) # Probabilidades de transición del estado 1

# Matriz de probabilidad de emisión
modelo_hmm.emissionprob_ = np.array([[0.1, 0.4, 0.5],  # Probabilidades de emisión del estado 0
                                     [0.6, 0.3, 0.1]]) # Probabilidades de emisión del estado 1

# Secuencia de observaciones
observaciones = np.array([[0, 1, 2, 2]])

# Ajustar el modelo HMM a las observaciones
modelo_hmm.fit(observaciones)

# Generar muestras de la secuencia de observaciones
muestras, estados = modelo_hmm.sample(5)

# Imprimir las muestras generadas y los estados correspondientes
print("Muestras generadas:", muestras)
print("Estados correspondientes:", estados)
