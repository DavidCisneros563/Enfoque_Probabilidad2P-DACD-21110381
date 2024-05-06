#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
from scipy.stats import chi2_contingency

# Definir los datos de las variables aleatorias
# Supongamos que tenemos dos variables aleatorias A y B
# A puede tomar los valores [0, 1] y B puede tomar los valores [0, 1]
# Definimos una tabla de contingencia que representa la frecuencia de ocurrencia conjunta de A y B
# En este ejemplo, asumimos que A y B son independientes si la tabla de contingencia sigue una distribución uniforme
tabla_contingencia = np.array([[30, 20], [20, 30]])

# Realizar el test de independencia condicional (Chi-cuadrado)
chi2, p, dof, expected = chi2_contingency(tabla_contingencia)

# Imprimir los resultados
print("Estadístico chi-cuadrado:", chi2)
print("Valor p:", p)
print("Grados de libertad:", dof)
print("Frecuencias esperadas:")
print(expected)
if p < 0.05:
    print("Se rechaza la hipótesis nula: A y B no son independientes.")
else:
    print("No se puede rechazar la hipótesis nula: A y B son independientes.")