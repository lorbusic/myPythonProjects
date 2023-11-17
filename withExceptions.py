
class TheClass:
    def divide(a,b):
        try:
            return a//b
        except ZeroDivisionError as e:
            print(e.args)
        else:
            print(" 'Else' can be used just after all 'except' claues and befory 'finally' ")
            print(" 'Else' is invoked if no exception happens ")
        finally:
            print("I am executed always")
     
    def divid(a,b): 
        return a//b
    
    
#z=TheClass.divide(1,0)
#print(z)
y=TheClass.divide(30,10)
print(y)
x=TheClass.divide(30,1)
print(x)

#RAISE

#for i in range(50):
    #print(i)
    #raise IndexError("Loop error")
 
#try:
#    c=TheClass.divid(4,0)
#except ZeroDivisionError:
#    print("Error div 0")
#    raise

x = 10
assert x == 5, "Not equal to 5"