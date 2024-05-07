#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar el filtro de Canny para detección de bordes
bordes = cv2.Canny(imagen_gris, 100, 200)

# Aplicar la segmentación por umbralización
_, segmentacion = cv2.threshold(imagen_gris, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes originales y procesadas
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 3, 2)
plt.imshow(bordes, cmap='gray')
plt.title('Detección de Bordes')

plt.subplot(1, 3, 3)
plt.imshow(segmentacion, cmap='gray')
plt.title('Segmentación por Umbralización')

plt.show()