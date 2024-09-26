class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"name is {self.name}, age is {self.age}"

p=Person('abhinand',21)
print(p)