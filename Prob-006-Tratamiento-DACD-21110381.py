#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk.corpus import brown
from nltk.util import ngrams
from collections import Counter

# Descargar los datos del corpus Brown si no están descargados
nltk.download('brown')

# Obtener el corpus Brown y dividirlo en oraciones
corpus = brown.sents()

# Obtener los trigramas del corpus
trigramas = [ngrams(sentencia, 3, pad_left=True, pad_right=True, pad_symbol='<s>') for sentencia in corpus]

# Contar la frecuencia de los trigramas
frecuencia_trigramas = Counter([trigrama for sent_trigramas in trigramas for trigrama in sent_trigramas])

# Calcular la probabilidad de una oración dada
def calcular_probabilidad_oracion(oracion):
    oracion_trigramas = list(ngrams(oracion, 3, pad_left=True, pad_right=True, pad_symbol='<s>'))
    probabilidad = 1.0
    for trigrama in oracion_trigramas:
        probabilidad_trigrama = frecuencia_trigramas[trigrama] / sum(frecuencia_trigramas.values())
        probabilidad *= probabilidad_trigrama
    return probabilidad

# Ejemplo de una oración
oracion_ejemplo = ['The', 'cat', 'sat', 'on', 'the', 'mat']
probabilidad_ejemplo = calcular_probabilidad_oracion(oracion_ejemplo)
print("La probabilidad de la oración:", oracion_ejemplo, "es:", probabilidad_ejemplo)
