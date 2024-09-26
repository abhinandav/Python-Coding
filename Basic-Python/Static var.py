class Mark:
    total=0
    def __init__(self,name ):
        self.name=name
        Mark.total=50
    
    def display(self):
        print(f"Name: {self.name}")

    @staticmethod
    def get_total():
        print(f"Total: {Mark.total}")

m=Mark('abhinand')

m.display()
m.get_total()