#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np

class MantoDeMarkov:
    def __init__(self, matriz_transicion):
        self.matriz_transicion = matriz_transicion
        self.num_estados = len(matriz_transicion)
        self.estado_actual = np.random.choice(self.num_estados)  # Estado inicial aleatorio

    def transicion(self):
        # Realizar una transición de estado
        self.estado_actual = np.random.choice(self.num_estados, p=self.matriz_transicion[self.estado_actual])

    def generar_secuencia(self, num_pasos):
        # Generar una secuencia de estados
        secuencia = [self.estado_actual]
        for _ in range(num_pasos - 1):
            self.transicion()
            secuencia.append(self.estado_actual)
        return secuencia

# Ejemplo de uso
matriz_transicion = np.array([[0.8, 0.2],
                               [0.4, 0.6]])  # Matriz de transición, filas representan el estado actual y columnas representan el siguiente estado
manto = MantoDeMarkov(matriz_transicion)

# Generar una secuencia de estados de longitud 10
secuencia_generada = manto.generar_secuencia(10)
print("Secuencia generada:", secuencia_generada)