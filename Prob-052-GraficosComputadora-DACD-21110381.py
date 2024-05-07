#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import matplotlib.pyplot as plt

# Generar datos para la función seno
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Graficar la función seno
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = sin(x)', color='blue')
plt.title('Gráfico de la función seno')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
