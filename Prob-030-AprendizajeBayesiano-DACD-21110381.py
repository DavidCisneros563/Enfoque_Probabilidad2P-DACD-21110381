#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Datos observados (muestras)
datos = np.array([1.2, 1.5, 1.8, 2.1, 2.4])

# Distribución a priori para la media (mu) y la desviación estándar (sigma)
media_priori = 0  # Media priori
desviacion_priori = 1  # Desviación estándar priori

# Parámetros de la distribución a priori para la media y la desviación estándar
# Estos pueden ser ajustados según el conocimiento previo o las creencias iniciales
# Por ejemplo, si se tiene confianza en que la media está cerca de 0 y la desviación estándar es pequeña, se pueden ajustar los valores.
# En este ejemplo, usaremos valores arbitrarios para ilustrar el proceso.
media_mu = 0  # Media de la distribución a priori para mu
desviacion_sigma = 1  # Desviación estándar de la distribución a priori para sigma

# Parámetros de la distribución a posteriori para la media y la desviación estándar
media_posteriori = (media_mu * desviacion_priori**2 + np.sum(datos)) / (desviacion_priori**2 + len(datos))
desviacion_posteriori = np.sqrt(1 / (1 / desviacion_priori**2 + len(datos) / desviacion_sigma**2))

# Estimación de la media y la desviación estándar posteriori
print("Media posteriori:", media_posteriori)
print("Desviación estándar posteriori:", desviacion_posteriori)
