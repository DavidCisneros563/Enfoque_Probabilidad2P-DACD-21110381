#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
modelo = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, 
                   values=[[0.3, 0.05, 0.9, 0.5], 
                           [0.4, 0.25, 0.08, 0.3], 
                           [0.3, 0.7, 0.02, 0.2]],
                   evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99], [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD(variable='S', variable_card=2, 
                   values=[[0.95, 0.2], [0.05, 0.8]],
                   evidence=['I'], evidence_card=[2])

# Agregar las CPDs al modelo
modelo.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Verificar si las CPDs son consistentes con la estructura del modelo
print("¿Las CPDs son consistentes con la estructura del modelo?", modelo.check_model())

# Realizar inferencia utilizando eliminación de variables
inferencia = VariableElimination(modelo)

# Calcular la probabilidad condicional P(L | D=1, I=0)
resultado = inferencia.query(variables=['L'], evidence={'D': 1, 'I': 0})
print("Probabilidad condicional P(L | D=1, I=0):")
print(resultado)
