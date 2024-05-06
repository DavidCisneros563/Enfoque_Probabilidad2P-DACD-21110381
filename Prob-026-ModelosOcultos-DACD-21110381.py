#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from hmmlearn import hmm
import numpy as np

# Definir el modelo HMM hacia atrás
modelo_bhmm = hmm.BackwardHMM(n_components=2, n_iter=100)

# Establecer las matrices de transición y de emisión
modelo_bhmm.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
modelo_bhmm.emissionprob_ = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])  # Matriz de emisión

# Generar secuencia de observaciones
observaciones = np.array([[0], [1], [2], [2]])

# Entrenar el modelo con la secuencia de observaciones
modelo_bhmm.fit(observaciones)

# Calcular la probabilidad de la secuencia de observaciones
probabilidad_secuencia = modelo_bhmm.score(observaciones)

print("Probabilidad de la secuencia de observaciones:", probabilidad_secuencia)
