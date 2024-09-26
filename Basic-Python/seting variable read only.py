class Person:
    def __init__(self,a):
        self._a=a
    
    @property
    def view(self):
        return self._a
    
p=Person(10)

try:
    p._a=10
except AttributeError as e:
    print(e)