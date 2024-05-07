#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

import nltk
from nltk import PCFG, Nonterminal, CFG

# Definir la gramática probabilística
gramatica_pcfg = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.7] | NP PP [0.3]
    VP -> V NP [0.6] | VP PP [0.4]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'man' [0.5] | 'dog' [0.3] | 'cat' [0.2]
    V -> 'chased' [0.6] | 'saw' [0.4]
    P -> 'in' [0.4] | 'on' [0.3] | 'by' [0.3]
""")

# Generar una oración aleatoria de acuerdo a la gramática
produccion = gramatica_pcfg.productions(Nonterminal('S'))[0]
oracion_generada = ''.join(produccion.lhs().symbol() for produccion in produccion.rhs())

print("Oración generada:", oracion_generada)