def decorator(f):
    def inner(s):
        if s:
            s='Hello '+ s
        return f(s)
    return inner

@decorator
def greet(s):
    print(s)

greet('abhinand')