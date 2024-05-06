#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

# Función para calcular la verosimilitud de un parámetro mu dada una muestra y la desviación estándar conocida
def verosimilitud(mu, muestra, desviacion_estandar):
    return np.prod(1 / (np.sqrt(2 * np.pi) * desviacion_estandar) * np.exp(-0.5 * ((muestra - mu) / desviacion_estandar)**2))

# Datos observados
muestra = np.array([1.2, 1.5, 1.8, 2.1, 2.4])

# Desviación estándar conocida
desviacion_estandar = 0.5

# Valores candidatos para el parámetro mu
valores_mu = np.linspace(0, 3, 100)

# Calcular la verosimilitud de cada valor candidato de mu
verosimilitudes = [verosimilitud(mu, muestra, desviacion_estandar) for mu in valores_mu]

# Normalizar las verosimilitudes para que sumen 1
verosimilitudes_normalizadas = verosimilitudes / np.sum(verosimilitudes)

# Calcular la media ponderada de mu utilizando las verosimilitudes normalizadas como pesos
mu_estimado = np.sum(valores_mu * verosimilitudes_normalizadas)
print("Estimación de mu:", mu_estimado)