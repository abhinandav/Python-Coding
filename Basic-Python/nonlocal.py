def outer():
    x='local'
    def inner():
        nonlocal x
        x='nonlocal'
    inner()
    print(x)

outer()


def outer():
    x='local'
    def inner():
        y='ll'
        def inner2():
            nonlocal x
            x='nonlocal'
    inner()
    print(x)

outer()
