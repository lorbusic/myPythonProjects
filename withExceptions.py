
class TheClass:
    def divide(a,b):
        try:
            return a//b
        except ZeroDivisionError:
            return "You can't divide by zero"
    
z=TheClass.divide(1,0)
print(z)
y=TheClass.divide(30,10)
print(y)