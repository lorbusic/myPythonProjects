
class BClass:
    def setMessage(self,message):
        self.message = message
    
    def printMessage(self):
        print(self.message)

class AClass(BClass):
    def printMessage(self): #it makes the Override: the method is overwritten 
                            #and the method in AClass is the considered method
        print("AClass: "+self.message) #'message' attribute is inherited from BClass
    
m1 = AClass()
m1.setMessage("Hello, you're in AClass but this method is inherited from BClass")
m1.printMessage()