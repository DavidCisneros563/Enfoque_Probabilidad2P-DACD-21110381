#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

class ProbabilidadAPriori:
    def __init__(self, labels):
        self.labels = labels
        self.counts = {}

    def calcular_apriori(self, labels):
        total_samples = len(labels)
        for label in labels:
            if label in self.counts:
                self.counts[label] += 1
            else:
                self.counts[label] = 1

        apriori_probs = {}
        for label, count in self.counts.items():
            apriori_probs[label] = count / total_samples

        return apriori_probs

# Ejemplo de uso
labels = ['clase1', 'clase2', 'clase1', 'clase2', 'clase1', 'clase2', 'clase1', 'clase2', 'clase1', 'clase2']
prob_apriori_calculator = ProbabilidadAPriori(labels)
prob_apriori = prob_apriori_calculator.calcular_apriori(labels)
print("Probabilidad a priori de cada clase:")
print(prob_apriori)
