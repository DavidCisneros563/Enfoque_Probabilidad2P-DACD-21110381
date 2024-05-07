#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk.translate import IBMModel1
from nltk.corpus import comtrans

# Descargar el corpus de alineación de texto paralelo
nltk.download("comtrans")

# Obtener datos de entrenamiento
bitext = comtrans.aligned_sents()[:100]

# Separar datos en pares de oraciones
frase_frases = [(pair.words, pair.mots) for pair in bitext]

# Entrenar el modelo de traducción
modelo = IBMModel1(frase_frases, 5)

# Traducir una oración de ejemplo
oracion_entrada = "Je suis étudiant"
oracion_salida = modelo.translate(oracion_entrada.split())
print("Oración de entrada:", oracion_entrada)
print("Oración traducida:", " ".join(oracion_salida))