class BClass:
    def __init__(self,message):
        self.message=message
    
    def printMessage(self):
        print(self.message)

class AClass(BClass):
    def __init__(self, message, valore):
        super().__init__(message)
        self.valore=valore

m1 = AClass('Python',20)
print(m1.valore)
m1.printMessage()