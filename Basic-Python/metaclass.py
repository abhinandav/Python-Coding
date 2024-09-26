class SimpleMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a new class
class MyClass(metaclass=SimpleMeta):
    pass


instance = MyClass()
instance2 = MyClass()
