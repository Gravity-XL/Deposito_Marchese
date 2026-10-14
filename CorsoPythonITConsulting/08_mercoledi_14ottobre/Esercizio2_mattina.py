#classe padre persona
   #primo figlio studente, secondo figlio professore (devono avere applicato l'incapsulamento)
   
   #collegati fra loro in un secondo momento
   
   #studente nome ecc
   
   #prof materia 
   
   #ognuna delle due sottoclassi 1-2 metodi unici 
   
   #tutte le variabili all'interno di professore, private
   
   #variabili dentro persona pubblica, in professore e studente private
   
  #extra scuola creazione studenti, creazione professori 
   

class Persona:  #classe padre, nome ed età lasciati pubblici, metoto presentazione semplice per richiamarli
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentazione(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")
        
    # GETTER : il getter permette di ottenere e leggere il valore di un attributo
    def get_nome(self):
        return self.nome

    def get_eta(self):
        return self.eta

    # SETTER: modifica o imposta il valore di un attributo 
    def set_nome(self, nuovo_nome):
        self.nome = nuovo_nome

    def set_eta(self, nuova_eta):
        self.eta = nuova_eta

class Studente(Persona): #dichiaro classe persona, aggiungo solo voti privato
    
    def __init__(self, nome, eta, voti):  
        self.nome = nome #potevo fare anche super, domanda a mirko, ma è indifferente
        self.eta = eta  
        self.__voti = voti
        
    def calcola_media(self): #metodo semplice per calcolare vedia voti, probabilmente mi darà qualche errore se lascio vuoto o divido per zero, l'ho scritto per allenarmi a mettere i metodi all'interno e richiamarli
        return sum(self.__voti) / len(self.__voti)
    
    def presentazione(self): # oslito metodo presentazione con frase semplice, 
        print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} anni e la mia media è {self.calcola_media():.2f}.")
        
    def get_voti(self): #visualizzo voti
        return self.__voti

    def set_voti(self, nuovi_voti): #modifico voti
        self.__voti = nuovi_voti

class Professore(Persona): #professore ha come attributo privato la materia a sto giro
    
    def __init__(self, nome, eta, materia):
        self.nome = nome #self.getnome self.geteta (mirko nella spiegazione dell'esercizio)
        self.eta = eta
        self.__materia = materia
        
        #esempio
        
       # def get materia(self):
           # return self.__materia
    
    def presentazione(self): #solita presentazione
        print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} anni e insegno {self.__materia}.")
        
    def get_materia(self): #richiamo materia
        return self.__materia

    def set_materia(self, nuova_materia): #modifico materia
        self.__materia = nuova_materia
   


# oggetti test pervedere se funziona

persona1 = Persona("Luca", 34)

studente1 = Studente("Dario", 22, [7, 7, 9, 10])

professore1 = Professore("Marco", 50, "Matematica")


#preesentazioni  test per vedere se funziona

persona1.presentazione()
studente1.presentazione()
professore1.presentazione()

