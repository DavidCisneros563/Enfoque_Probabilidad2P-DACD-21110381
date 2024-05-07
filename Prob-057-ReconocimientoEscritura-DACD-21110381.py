#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import pytesseract
from PIL import Image

# Cargar la imagen con texto manuscrito
imagen = Image.open("texto_manuscrito.png")

# Utilizar pytesseract para reconocer el texto
texto_reconocido = pytesseract.image_to_string(imagen, lang='spa')

# Imprimir el texto reconocido
print("Texto reconocido:")
print(texto_reconocido)

