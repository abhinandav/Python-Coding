from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age:int
    
p=Person(name='abhinand',age=21)

print(p)
