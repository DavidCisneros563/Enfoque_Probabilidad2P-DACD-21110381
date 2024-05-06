#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

def forward_algorithm(observaciones, A, B, pi):
    T = len(observaciones)
    N = len(A)
    
    # Paso hacia adelante
    alpha = np.zeros((T, N))
    alpha[0] = pi * B[:, observaciones[0]]
    for t in range(1, T):
        alpha[t] = np.dot(alpha[t-1], A) * B[:, observaciones[t]]
    
    return alpha

def backward_algorithm(observaciones, A, B):
    T = len(observaciones)
    N = len(A)
    
    # Paso hacia atrás
    beta = np.ones((T, N))
    for t in range(T-2, -1, -1):
        beta[t] = np.dot(A, B[:, observaciones[t+1]] * beta[t+1])
    
    return beta

def forward_backward_algorithm(observaciones, A, B, pi):
    T = len(observaciones)
    N = len(A)
    
    # Paso hacia adelante
    alpha = forward_algorithm(observaciones, A, B, pi)
    
    # Paso hacia atrás
    beta = backward_algorithm(observaciones, A, B)
    
    # Calcular la probabilidad marginal de cada estado en cada tiempo
    gamma = alpha * beta / np.sum(alpha[-1])
    
    return gamma

# Definir el modelo oculto de Markov (HMM)
A = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición de estado
B = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])  # Matriz de emisión
pi = np.array([0.6, 0.4])  # Distribución inicial de estado

# Secuencia de observaciones
observaciones = [0, 1, 2, 2]

# Aplicar el algoritmo hacia adelante-atrás para calcular las probabilidades marginales
probabilidades_marginales = forward_backward_algorithm(observaciones, A, B, pi)
print("Probabilidades marginales de los estados ocultos:")
print(probabilidades_marginales)
