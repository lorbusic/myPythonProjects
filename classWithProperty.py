
class MyClass():
    def __init__(self, my_attr):
        self.__priv_attr=my_attr

    @property #decorator for getter method
    def attr(self):
        return self.__priv_attr
    
    @attr.setter #decorator for setter method
    def attr(self,attr):
        self.__priv_attr=attr
     

obj = MyClass('python')
print(obj.attr)  
obj.attr='hello'
print(obj.attr)  

#print(obj.__priv_attr)

#attributes that are preceded by double underscore are not visible at the outside of class