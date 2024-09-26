class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name=name

p=Person('abhinand',21)

print(p.get_name())

