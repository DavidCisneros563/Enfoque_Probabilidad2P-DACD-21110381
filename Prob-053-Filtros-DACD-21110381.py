#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro de suavizado Gaussiano
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar filtro de detección de bordes
imagen_bordes = cv2.Canny(imagen, 100, 200)

# Mostrar las imágenes originales y procesadas
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 3, 2)
plt.imshow(imagen_suavizada, cmap='gray')
plt.title('Imagen Suavizada')

plt.subplot(1, 3, 3)
plt.imshow(imagen_bordes, cmap='gray')
plt.title('Detección de Bordes')

plt.show()
