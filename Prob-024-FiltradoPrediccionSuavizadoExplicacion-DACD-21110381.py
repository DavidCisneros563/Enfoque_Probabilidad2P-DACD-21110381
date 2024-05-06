#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from filterpy.kalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

# Modelo del sistema
dt = 1.0  # Intervalo de tiempo
F = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])  # Matriz de observación

# Proceso de ruido
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del proceso de ruido
R = 5  # Covarianza del ruido de medición

# Inicialización del filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)
kf.x = np.array([0, 0])  # Estado inicial
kf.P = np.eye(2)  # Matriz de covarianza inicial
kf.F = F
kf.H = H
kf.Q = Q
kf.R = R

# Simulación de observaciones
num_pasos = 50
observaciones = [10 + np.random.randn() * np.sqrt(R) for _ in range(num_pasos)]

# Filtrado, predicción y suavizado
estados_filtrados = []
estados_predichos = []
estados_suavizados = []

for z in observaciones:
    kf.predict()  # Predicción del estado siguiente
    kf.update(z)  # Actualización del estado basado en la observación actual
    estados_filtrados.append(kf.x[0])
    estados_predichos.append(kf.x_prior[0])
    estados_suavizados.append(kf.x_post[0])

# Visualización de resultados
plt.figure(figsize=(12, 6))
plt.plot(observaciones, 'ro', label='Observaciones')
plt.plot(estados_filtrados, 'g-', label='Estados Filtrados')
plt.plot(estados_predichos, 'b--', label='Estados Predichos')
plt.plot(estados_suavizados, 'm-.', label='Estados Suavizados')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Filtrado, Predicción y Suavizado con Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()
