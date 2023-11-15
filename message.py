class MyClass:
   
    def __init__(self,message):
        self.message=message
    
    def changeMess(self,message):
        self.message=message

    def printMessage(self):
        print(self.message)


m1 = MyClass("ciao") 
m1.printMessage()
m1.changeMess("bye bye")
m1.printMessage()
m2 = MyClass("hello") 
m2.printMessage()

    