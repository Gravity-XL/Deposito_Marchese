class Luca: #definizione di classe
    
    nome = "Luca"  #variabile di classe
    
    #metodo di classe
    def saluta(self):
        return("Ciao Luca")
    
    def __init__(self,nome:str, eta:int):
        self.nome = nome
        self.eta = eta
        
    
    
Ogg_1 = Luca()  #sto istanziando un dato
Ogg_2 = Luca() 

Ogg_2.nome = "Dario"  

print(Ogg_1.nome)
print(Ogg_2.nome)

print(Ogg_1.saluta())

#ogni classe può essere definita una volta sola


class Persona: #definizione di classe
    
    #metodo costruttore, "persona" in questo caso
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
        
    #il self è il nome proprio dell'oggetto
    
    
    #il metodo costruttore sta aspettando il parametro self ed eta, il self è il nome dell'oggetto, ed eta dentro la parentesi
    #posso mettere anche piu parametri nel metodo costruttore, ad esempio self per richiamare l'oggetto, "nome", ed "eta"
    
   #quindi il costruttore serve a creare l'oggetto ep uò richiedere parametri obblgatori, dati nell'ordine richiesto 
    
    nome = "Persona"  #variabile di classe
    
    #metodo di classe
    
    def saluta (self):
        return ("Ciao")
    
    
Ogg_1 = Persona("Luca", 34)  #sto istanziando nome ed eta
Ogg_2 = Persona("Dario", 40) #sto istanziando nome ed eta

Ogg_2.nome = "Dario"  

print(Ogg_1.nome)
print(Ogg_2.nome)

#ogni classe può essere definita una volta sola


class Automobile:    #dichiaro la classe 
    
    numero_di_ruote = 4    #attributo di classe 
    
    def __init__(self, marca, modello):  #metodo costruttore
        
        self.marca = marca  #attributo di istanza, lo scrivo perchè quell'istanza dice.. il self dirà oggetto 1 è uguale alla marca che ti sto passando
        self.modello=modello   #attributo di istanza
        
    def stampa_info(self):   #metodo di istanza
        
        print("L'automobile è una", self.marca, self.modello)
        
        #CREAZIONI DI OGGETTI DA UNA CLASSE 
        
Auto1 = Automobile("Fiat", "500")
Auto2 = Automobile("BMW", "X3")
#DA COMPLETARE PAG 111 CIRCA



class Esempio:
    pass

Es = Esempio #sia scritto che non scritto il metodo speciale della classe, esiste, noi possiamo solo modificarlo
    #ma nel momento che esiste una classe ESISTE SEMPRE, GIA', NON PUO ESSERE ELINIMATO 
    
    
    #__________METODO STATICO_____
    
class Calcolatrice:
    
    @staticmethod
    def somma(a, b):
        return a + b 
    
#Uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5,3)

print(risultato)
#Output: 8
    
    