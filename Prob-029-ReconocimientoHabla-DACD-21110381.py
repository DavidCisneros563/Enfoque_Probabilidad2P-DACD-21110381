#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import speech_recognition as sr

# Crear un objeto Recognizer
recognizer = sr.Recognizer()

# Capturar audio desde el micrófono
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

# Utilizar Google Speech Recognition para convertir audio en texto
try:
    texto = recognizer.recognize_google(audio, language="es-ES")  # Especifica el idioma
    print("Texto reconocido:", texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print("Error al solicitar resultados desde Google Speech Recognition service:", e)
    