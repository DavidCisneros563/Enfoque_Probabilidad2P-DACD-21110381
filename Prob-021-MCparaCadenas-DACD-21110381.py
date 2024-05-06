#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Función de densidad de probabilidad objetivo (distribución de probabilidad que queremos muestrear)
def pdf_objetivo(x):
    return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

# Función de densidad de probabilidad propuesta (distribución de probabilidad de la que podemos muestrear fácilmente)
def pdf_propuesta(x, sigma):
    return np.random.normal(x, sigma)

# Algoritmo de Metropolis-Hastings
def metropolis_hastings(pdf_objetivo, pdf_propuesta, num_muestras, sigma):
    muestras = []
    x_actual = 0  # Valor inicial arbitrario
    for _ in range(num_muestras):
        x_propuesto = pdf_propuesta(x_actual, sigma)
        aceptacion = min(1, pdf_objetivo(x_propuesto) / pdf_objetivo(x_actual))
        if np.random.uniform(0, 1) < aceptacion:
            x_actual = x_propuesto
        muestras.append(x_actual)
    return muestras

# Parámetros
num_muestras = 10000
sigma = 1

# Generar muestras utilizando el algoritmo de Metropolis-Hastings
muestras = metropolis_hastings(pdf_objetivo, pdf_propuesta, num_muestras, sigma)

# Imprimir resultados
print("Muestras generadas utilizando Metropolis-Hastings:")
print(muestras)
