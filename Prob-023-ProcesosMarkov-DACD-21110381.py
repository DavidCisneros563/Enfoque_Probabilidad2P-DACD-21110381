#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class ProcesoMarkov:
    def __init__(self, matriz_transicion, estados):
        self.matriz_transicion = matriz_transicion
        self.estados = estados
        self.estado_actual = np.random.choice(estados)  # Estado inicial aleatorio

    def transicion(self):
        # Realizar una transición de estado
        self.estado_actual = np.random.choice(self.estados, p=self.matriz_transicion[self.estado_actual])

    def generar_secuencia(self, num_pasos):
        # Generar una secuencia de estados
        secuencia = [self.estado_actual]
        for _ in range(num_pasos - 1):
            self.transicion()
            secuencia.append(self.estado_actual)
        return secuencia

# Ejemplo de uso
matriz_transicion = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}
estados = ['A', 'B']

proceso = ProcesoMarkov(matriz_transicion, estados)

# Generar una secuencia de estados de longitud 10
secuencia_generada = proceso.generar_secuencia(10)
print("Secuencia generada:", secuencia_generada)
