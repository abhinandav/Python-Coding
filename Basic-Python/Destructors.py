class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"name is {self.name} and age is {self.age}")
    
    def __del__(self):
        print(f"{self.name} is deleted")



p=Person('abhinand',21)
p.display()
del p
