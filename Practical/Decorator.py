def decorator(fn):
    def inner(a,b):
        if b==0:
            print('cant divisble by zero')
            return
        return fn(a,b)
    return inner

@decorator
def div(a,b):
    print(a/b)


div(10,0)