#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial
import speech_recognition as sr
import pandas as pd

# Función para realizar el reconocimiento de voz
def reconocimiento_voz():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Di algo:")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para el ruido del ambiente
        audio = recognizer.listen(source)
    
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print("Has dicho:", texto)
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        return None
    except sr.RequestError as e:
        print("Error al conectarse al servicio de reconocimiento de voz; {0}".format(e))
        return None

# Función para analizar el texto reconocido
def analizar_texto(texto):
    # Aquí puedes implementar tu lógica de análisis de texto basado en probabilidades
    # Por ejemplo, podrías utilizar un modelo de lenguaje probabilístico o reglas de gramática
    
    # En este ejemplo, simplemente dividimos el texto en palabras y contamos la frecuencia de cada palabra
    palabras = texto.split()
    frecuencia_palabras = pd.Series(palabras).value_counts()
    print("Frecuencia de palabras:")
    print(frecuencia_palabras)

# Ejecutar el reconocimiento de voz y análisis de texto
texto_reconocido = reconocimiento_voz()
if texto_reconocido:
    analizar_texto(texto_reconocido)
