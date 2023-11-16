
class MyClass():
    def __init__(self, my_attr):
        self.__priv_attr=my_attr

    def get_attr(self):
        return self.__priv_attr

    def set_attr(self,attr):
        self.__priv_attr=attr
    
    attr = property(get_attr,set_attr)

obj = MyClass('python')
print(obj.attr)
obj.attr='prova'
print(obj.attr)

obj.set_attr('the try')
print(obj.get_attr())
#print(obj.__priv_attr)

#attributes that are preceded by double underscore are not visible at the outside of class