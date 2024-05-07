#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import cv2

# Cargar el modelo pre-entrenado MobileNet SSD
modelo = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")

# Clases de objetos que el modelo puede detectar
clases = ["fondo", "avion", "bicicleta", "ave", "bote", "botella", "autobus", "auto", "gato", "silla"]

# Cargar la imagen
imagen = cv2.imread("imagen.jpg")
alto, ancho = imagen.shape[:2]

# Pre-procesar la imagen (escalarla, normalizarla, etc.)
imagen_preprocesada = cv2.dnn.blobFromImage(cv2.resize(imagen, (300, 300)), 0.007843, (300, 300), 127.5)

# Pasar la imagen preprocesada al modelo y realizar la detección de objetos
modelo.setInput(imagen_preprocesada)
detecciones = modelo.forward()

# Iterar sobre las detecciones y dibujar rectángulos alrededor de los objetos detectados
for i in range(detecciones.shape[2]):
    confianza = detecciones[0, 0, i, 2]
    if confianza > 0.5:  # Umbral de confianza
        indice_clase = int(detecciones[0, 0, i, 1])
        x1, y1, x2, y2 = (detecciones[0, 0, i, 3:7] * np.array([ancho, alto, ancho, alto])).astype(int)
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        etiqueta = "{}: {:.2f}%".format(clases[indice_clase], confianza * 100)
        cv2.putText(imagen, etiqueta, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con las detecciones
cv2.imshow("Detección de Objetos", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
