from abc import ABC,abstractmethod

class Mileage(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Mileage):
    def mileage(self):
        print('50 km')

class Maruti(Mileage):
    def mileage(self):
        print('20 km')