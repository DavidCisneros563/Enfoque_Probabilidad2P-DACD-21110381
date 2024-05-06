#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

def muestreo_directo(modelo, num_muestras):
    muestras = []
    for _ in range(num_muestras):
        muestra = {}
        for variable in modelo:
            probabilidad = modelo[variable]
            valor = np.random.choice(probabilidad['valores'], p=probabilidad['probabilidades'])
            muestra[variable] = valor
        muestras.append(muestra)
    return muestras

# Ejemplo de uso
modelo_probabilistico = {
    'A': {'valores': [0, 1], 'probabilidades': [0.7, 0.3]},
    'B': {'valores': [0, 1], 'probabilidades': [0.6, 0.4]}
}
muestras_directas = muestreo_directo(modelo_probabilistico, 100)
print("Muestras generadas por muestreo directo:")
print(muestras_directas)
