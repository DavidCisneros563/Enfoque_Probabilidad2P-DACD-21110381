#David Alejandro Cisneros Delgadillo
#21110381
#6E1
#Inteligencia Artificial

# Implementación de la Regla de Bayes para clasificación binaria

class ReglaDeBayes:
    def __init__(self, prob_spam, prob_no_spam, prob_palabra_dado_spam, prob_palabra_dado_no_spam):
        self.prob_spam = prob_spam
        self.prob_no_spam = prob_no_spam
        self.prob_palabra_dado_spam = prob_palabra_dado_spam
        self.prob_palabra_dado_no_spam = prob_palabra_dado_no_spam

    def clasificar(self, palabras):
        prob_spam_dado_palabras = self.prob_spam
        prob_no_spam_dado_palabras = self.prob_no_spam

        for palabra in palabras:
            if palabra in self.prob_palabra_dado_spam:
                prob_spam_dado_palabras *= self.prob_palabra_dado_spam[palabra]
            if palabra in self.prob_palabra_dado_no_spam:
                prob_no_spam_dado_palabras *= self.prob_palabra_dado_no_spam[palabra]

        return prob_spam_dado_palabras > prob_no_spam_dado_palabras

# Ejemplo de uso
prob_spam = 0.4
prob_no_spam = 0.6
prob_palabra_dado_spam = {'oferta': 0.8, 'urgente': 0.7, 'ganador': 0.6}
prob_palabra_dado_no_spam = {'oferta': 0.1, 'urgente': 0.2, 'ganador': 0.3}

modelo_bayes = ReglaDeBayes(prob_spam, prob_no_spam, prob_palabra_dado_spam, prob_palabra_dado_no_spam)

correo_ejemplo = ['oferta', 'urgente']
es_spam = modelo_bayes.clasificar(correo_ejemplo)

if es_spam:
    print("El correo electrónico es spam.")
else:
    print("El correo electrónico no es spam.")