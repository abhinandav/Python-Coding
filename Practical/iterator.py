class Iterator:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    
it=Iterator()
i=iter(it)
print(next(i))
print(next(i))
print(next(i))
