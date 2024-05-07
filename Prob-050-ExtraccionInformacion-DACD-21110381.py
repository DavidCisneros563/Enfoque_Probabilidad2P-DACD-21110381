#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import spacy

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_sm")

# Definir una función para realizar la extracción de información
def extraer_informacion(texto):
    doc = nlp(texto)
    entidades = [(entidad.text, entidad.label_) for entidad in doc.ents]
    return entidades

# Texto de ejemplo
texto = "El presidente de Estados Unidos, Joe Biden, anunció un nuevo plan para la infraestructura."

# Realizar la extracción de información
informacion_extraida = extraer_informacion(texto)

# Mostrar los resultados
print("Entidades encontradas:")
for entidad, tipo in informacion_extraida:
    print("- Entidad: {}, Tipo: {}".format(entidad, tipo))
