

#ESERCIZIO DA COMPLETARE CON CALMA

#si manifesta in modificatori, protetti e privati doppio trattino, metodi getter e setter (metodi normali)
#dichiarate o meno nell'init non cambia nulla o lasciarle vuote
#get 

class ContoBancario:

    def __init__(self,titolare,saldo):
        self.__titolare = titolare
        self.__saldo = saldo
        
 
#getter 
 
    def get_titolare(self):
        return self.__titolare


    def get_saldo(self):
        return self.__saldo

#setter

    def set_titolare(self):
        pass


    def set_saldo(self):
        pass
    
