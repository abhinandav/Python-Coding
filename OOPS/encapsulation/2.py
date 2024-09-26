class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self._age=age



person = Person("Alice", 30)
print(person.age)    
person.age = 35 
print(person.age)    
