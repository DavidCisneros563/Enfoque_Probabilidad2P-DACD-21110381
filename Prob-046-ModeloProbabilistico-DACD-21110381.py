#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from collections import defaultdict

class ModeloProbabilisticoLenguaje:
    def __init__(self, corpus):
        self.unigramas = defaultdict(int)
        self.bigramas = defaultdict(lambda: defaultdict(int))
        self.entrenar(corpus)
    
    def entrenar(self, corpus):
        for palabra in corpus.split():
            self.unigramas[palabra] += 1
        
        palabras = corpus.split()
        for i in range(len(palabras) - 1):
            palabra_actual, palabra_siguiente = palabras[i], palabras[i + 1]
            self.bigramas[palabra_actual][palabra_siguiente] += 1
    
    def probabilidad_unigrama(self, palabra):
        total_palabras = sum(self.unigramas.values())
        return self.unigramas[palabra] / total_palabras if total_palabras > 0 else 0
    
    def probabilidad_bigrama(self, palabra_actual, palabra_siguiente):
        total_bigramas = sum(self.bigramas[palabra_actual].values())
        return self.bigramas[palabra_actual][palabra_siguiente] / total_bigramas if total_bigramas > 0 else 0

# Ejemplo de uso
corpus = "el gato está sobre la mesa el perro está bajo la mesa"
modelo = ModeloProbabilisticoLenguaje(corpus)

# Calcular la probabilidad de unigrama de la palabra "el"
print("Probabilidad de 'el':", modelo.probabilidad_unigrama("el"))

# Calcular la probabilidad de bigrama de "la mesa"
print("Probabilidad de bigrama 'la mesa':", modelo.probabilidad_bigrama("la", "mesa"))
