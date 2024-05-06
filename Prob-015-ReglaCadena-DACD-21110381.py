#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# Definir las probabilidades condicionales P(X | Y, Z), P(Y | Z) y P(Z)
prob_condicional_X_dado_YZ = 0.8
prob_condicional_Y_dado_Z = 0.6
prob_Z = 0.5

# Calcular la probabilidad conjunta P(X, Y, Z) utilizando la regla de la cadena
prob_conjunta_XYZ = prob_condicional_X_dado_YZ * prob_condicional_Y_dado_Z * prob_Z

# Imprimir el resultado
print("Probabilidad conjunta P(X, Y, Z) utilizando la regla de la cadena:", prob_conjunta_XYZ)