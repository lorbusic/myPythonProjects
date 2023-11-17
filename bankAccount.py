class Conto:
    def __init__(self,nome,conto):
        self.nome=nome
        self.conto=conto



class ContoCorrente(Conto):
    
    def __init__(self,nome,conto,importo):
        super().__init__(nome,conto)
        self.__saldo=float(importo)

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += float(importo)

    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    @property
    def saldo(self):
        print("I am in getter method")
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        print("I am in setter method")
        self.preleva(self.__saldo)
        self.deposita(importo)


class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)

c1 = ContoCorrente("Amy","93939","10420")
c1.descrizione()
c2 = ContoCorrente("Emma","91939","10320")
c2.descrizione()

GestoreContiCorrenti().bonifico(c1,c2,10)
print("Amy ha effettuato un bonifico di 10 euro a Emma")
c1.descrizione()
c2.descrizione()

#cc.saldo = 12030
#print(cc.saldo)

#c1 = ContoCorrente("Mario","88100","2500")
#c2 = ContoCorrente("Mariella","823100","3500")
#c1.descrizione()
#c2.descrizione()
#c1.deposita(200)
#c2.deposita(400)
#c1.descrizione()
#c2.descrizione()
#c1.preleva(100)
#c2.preleva(200)
#c1.descrizione()
#c2.descrizione()