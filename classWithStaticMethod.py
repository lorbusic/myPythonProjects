class MyClass:

    @staticmethod #this is a decorator
    def sum(a,b):
        return a+b

s = MyClass.sum(2,4) 
print(s)