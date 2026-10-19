# metodi speciali

#__str__ stabilisce come deve essere rappresentato un oggetto quando viene convertito in stringa, ad esempio con print().

class Studente:
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def __str__(self):
        return "Studente: " + self.nome + ",eta: " + str(self.eta)
    
studente1 = Studente("Luca", 20)

print(studente1)

#___________________

class Squadra: 
    
    def __init__(self, nome, giocatori):
        self.nome = nome
        self.giocatori = giocatori
    
    def __len__(self):
        return len(self.giocatori)
    
squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])

print(len(squadra1))


#__________

class Moltiplicatore:
    
    def __int__(self, numero):
        self.numero = numero
        
    def __call__(self, valore):
        return valore * self.numero
    
doppio = Moltiplicatore(2)

print(doppio(10))