from abc import abstractmethod,ABC

class Details(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def age(self):
        pass

class Person(Details):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def age(self):
        return self.age
    
