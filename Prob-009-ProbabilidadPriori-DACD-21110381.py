#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar un clasificador de Naive Bayes Gaussiano
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# Predecir las etiquetas en el conjunto de prueba
y_pred = naive_bayes.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador de Naive Bayes:", accuracy)