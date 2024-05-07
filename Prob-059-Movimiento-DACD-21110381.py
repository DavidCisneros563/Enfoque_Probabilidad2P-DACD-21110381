#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2

# Capturar el video desde la cámara (0 para la cámara predeterminada)
captura = cv2.VideoCapture(0)

# Leer el primer fotograma
ret, fotograma_anterior = captura.read()

while True:
    # Leer el siguiente fotograma
    ret, fotograma_actual = captura.read()

    # Convertir los fotogramas a escala de grises
    gris_anterior = cv2.cvtColor(fotograma_anterior, cv2.COLOR_BGR2GRAY)
    gris_actual = cv2.cvtColor(fotograma_actual, cv2.COLOR_BGR2GRAY)

    # Calcular la diferencia absoluta entre los fotogramas
    diferencia = cv2.absdiff(gris_anterior, gris_actual)

    # Aplicar un umbral para resaltar las áreas de movimiento
    umbral, mascara = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)

    # Encontrar los contornos de las áreas de movimiento
    contornos, jerarquia = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el fotograma actual
    cv2.drawContours(fotograma_actual, contornos, -1, (0, 255, 0), 2)

    # Mostrar el fotograma actual
    cv2.imshow('Deteccion de Movimiento', fotograma_actual)

    # Actualizar el fotograma anterior
    fotograma_anterior = fotograma_actual.copy()

    # Romper el bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar todas las ventanas
captura.release()
cv2.destroyAllWindows()
