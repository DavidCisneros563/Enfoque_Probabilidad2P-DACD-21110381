#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from filterpy.kalman import KalmanFilter
import numpy as np

# Definir el filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)  # Dimensión del estado y de la observación

# Definir las matrices de transición de estado y de observación
kf.F = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado (A)
kf.H = np.array([[1, 0]])  # Matriz de observación (H)

# Definir las matrices de covarianza del proceso y de ruido de medición
kf.Q = np.array([[0.001, 0.001], [0.001, 0.001]])  # Covarianza del proceso (Q)
kf.R = np.array([[0.1]])  # Covarianza del ruido de medición (R)

# Definir el estado inicial y la covarianza inicial
kf.x = np.array([[0], [0]])  # Estado inicial (x)
kf.P = np.eye(2)  # Covarianza inicial (P)

# Simular observaciones
observaciones = [10 + np.random.randn() * np.sqrt(kf.R[0, 0]) for _ in range(50)]

# Aplicar el filtro de Kalman para estimar el estado del sistema
estados_filtrados = []
for z in observaciones:
    kf.predict()  # Predicción del estado siguiente
    kf.update(z)  # Actualización del estado basado en la observación actual
    estados_filtrados.append(kf.x[0, 0])  # Estimar el estado

# Visualizar resultados
import matplotlib.pyplot as plt
plt.plot(observaciones, 'ro', label='Observaciones')  # Observaciones
plt.plot(estados_filtrados, 'g-', label='Estados Filtrados')  # Estados filtrados
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()
