# abstract class and abstract method

from abc import ABC,abstractmethod


class car(ABC):
    @abstractmethod
    def color(self):
        pass

    def tyre(self):
        self.num_tyre=4

class Maruti(car):
    def color(self):
        self.car_color='red'

    

m=Maruti()
m.color()
print(m.car_color)

m.tyre()
print(m.num_tyre)