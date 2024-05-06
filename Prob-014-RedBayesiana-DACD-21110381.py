#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
modelo = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=3,
                   values=[[0.1, 0.2, 0.3, 0.2],
                           [0.4, 0.4, 0.4, 0.4],
                           [0.5, 0.4, 0.3, 0.4]],
                   evidence=['A', 'B'], evidence_card=[2, 2])
cpd_d = TabularCPD(variable='D', variable_card=2,
                   values=[[0.9, 0.6, 0.1],
                           [0.1, 0.4, 0.9]],
                   evidence=['C'], evidence_card=[3])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c, cpd_d)

# Verificar si las CPDs son consistentes con la estructura del modelo
print("¿Las CPDs son consistentes con la estructura del modelo?", modelo.check_model())

# Realizar inferencia utilizando eliminación de variables
inferencia = VariableElimination(modelo)

# Calcular la probabilidad condicional P(D | A=1, B=0)
resultado = inferencia.query(variables=['D'], evidence={'A': 1, 'B': 0})
print("Probabilidad condicional P(D | A=1, B=0):")
print(resultado)