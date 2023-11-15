class classInvokeCounter:
    counter=0
    def __init__(self):
        classInvokeCounter.counter+=1

    def printCounter(self):
        print(classInvokeCounter.counter)

c1=classInvokeCounter()
c1.printCounter()
c2=classInvokeCounter()
c2.printCounter()
c3=classInvokeCounter()
c3.printCounter()
c4=classInvokeCounter()
c4.printCounter()
c5=classInvokeCounter()
c5.printCounter()
