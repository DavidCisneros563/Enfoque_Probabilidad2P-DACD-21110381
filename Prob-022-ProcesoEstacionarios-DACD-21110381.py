#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Parámetros del proceso AR
num_muestras = 1000
phi = 0.9  # Parámetro de autocorrelación

# Generar muestras del proceso AR
ruido = np.random.normal(0, 1, num_muestras)
proceso_ar = [ruido[0]]
for i in range(1, num_muestras):
    proceso_ar.append(phi * proceso_ar[i - 1] + ruido[i])

# Visualizar el proceso AR
plt.figure(figsize=(10, 5))
plt.plot(proceso_ar)
plt.title("Proceso AR con phi = {}".format(phi))
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()
