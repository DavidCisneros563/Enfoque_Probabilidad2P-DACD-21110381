#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generar datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 2)
y = np.random.randint(2, size=(100,))

# Definir el modelo MLP
modelo = Sequential([
    Dense(64, input_dim=2, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X, y, epochs=10, batch_size=32, verbose=1)

# Evaluar el modelo
loss, accuracy = modelo.evaluate(X, y)
print("Precisión del modelo:", accuracy)
