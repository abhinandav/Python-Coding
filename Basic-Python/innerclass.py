class outer:
    def __init__(self,a):
        self.a=a
    def display_outer(self):
        print(self.a)


    class inner:
        def __init__(self,b):
            self.b=b
        def display_inner(self):
            print(self.b)

o=outer(10)
o.display_outer()
inn=o.inner(20)
inn.display_inner()