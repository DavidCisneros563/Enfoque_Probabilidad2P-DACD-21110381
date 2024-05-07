#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class SistemaRecuperacionDatos:
    def __init__(self, datos):
        self.datos = datos
    
    def buscar(self, consulta):
        resultados = []
        for clave, valor in self.datos.items():
            if consulta.lower() in clave.lower() or consulta.lower() in valor.lower():
                resultados.append((clave, valor))
        return resultados

# Ejemplo de uso
datos = {
    "documento1": "Este es un documento de ejemplo",
    "documento2": "Otro documento con información interesante",
    "documento3": "Un tercer documento para demostración"
}

sistema = SistemaRecuperacionDatos(datos)

consulta = "documento"
resultados = sistema.buscar(consulta)

print("Resultados de la consulta '{}':".format(consulta))
for resultado in resultados:
    print("- Nombre: {}, Contenido: {}".format(resultado[0], resultado[1]))