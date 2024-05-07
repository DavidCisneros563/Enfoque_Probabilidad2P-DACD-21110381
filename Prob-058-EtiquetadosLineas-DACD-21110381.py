#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread("imagen.jpg")

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para obtener una imagen binaria
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos en la imagen binaria
contornos, jerarquia = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos y etiquetarlos
for i, contorno in enumerate(contornos):
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(imagen, f"Linea {i+1}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con los contornos etiquetados
cv2.imshow("Etiquetado de Lineas", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
