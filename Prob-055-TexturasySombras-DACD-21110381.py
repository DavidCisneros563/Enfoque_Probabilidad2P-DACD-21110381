#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2
import numpy as np

# Crear una imagen de fondo
fondo = np.zeros((300, 300, 3), dtype=np.uint8)
fondo.fill(255)  # Color blanco

# Definir las coordenadas de un polígono que representará un objeto
poligono = np.array([[50, 50], [250, 50], [200, 200], [100, 200]], np.int32)
poligono = poligono.reshape((-1, 1, 2))

# Dibujar el polígono en la imagen de fondo
cv2.fillPoly(fondo, [poligono], (0, 0, 0))  # Color negro para el objeto

# Definir la fuente de luz
fuente_luz = (150, 100)

# Calcular la sombra proyectada del polígono
sombra = np.zeros_like(fondo)
for i in range(poligono.shape[0]):
    punto = poligono[i, 0]
    dx = punto[0] - fuente_luz[0]
    dy = punto[1] - fuente_luz[1]
    cv2.line(sombra, fuente_luz, (fuente_luz[0] + dx, fuente_luz[1] + dy), (100, 100, 100), 2)

# Combinar la imagen de fondo con la sombra
imagen_con_sombra = cv2.addWeighted(fondo, 0.7, sombra, 0.3, 0)

# Mostrar la imagen resultante
cv2.imshow('Imagen con sombra', imagen_con_sombra)
cv2.waitKey(0)
cv2.destroyAllWindows()
