#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt

# Función de transición de estado (modelo de movimiento)
def transicion_estado(x, dt, velocidad, ruido_proceso):
    return x + velocidad * dt + np.random.randn() * np.sqrt(ruido_proceso)

# Función de observación (medida de posición)
def observacion(x, ruido_medicion):
    return x + np.random.randn() * np.sqrt(ruido_medicion)

# Parámetros del modelo
velocidad_real = 1.0
ruido_proceso = 0.1
ruido_medicion = 0.1

# Configuración del filtro de partículas
num_particulas = 1000
dt = 1.0
tiempo_total = 10
posicion_inicial = 0.0

# Inicialización de las partículas
particulas = np.random.normal(posicion_inicial, 1, num_particulas)

# Realizar el filtrado de partículas
posiciones_filtradas = []
for t in range(tiempo_total):
    # Predicción: mover las partículas según el modelo de transición de estado
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i], dt, velocidad_real, ruido_proceso)
    
    # Actualización: calcular el peso de cada partícula según la observación y normalizar los pesos
    pesos = np.exp(-0.5 * ((observacion(particulas, ruido_medicion) - t) / ruido_medicion)**2)
    pesos /= np.sum(pesos)
    
    # Resamplear partículas basado en sus pesos
    indices_resampleados = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
    particulas = particulas[indices_resampleados]
    
    # Calcular la posición estimada como la media de las partículas
    posicion_estimada = np.mean(particulas)
    posiciones_filtradas.append(posicion_estimada)

# Visualización de resultados
plt.figure(figsize=(10, 5))
plt.plot(np.arange(tiempo_total), posiciones_filtradas, label='Posición Filtrada')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Partículas')
plt.legend()
plt.grid(True)
plt.show()