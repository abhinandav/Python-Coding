def generator():
    i=0
    n=10
    while i<n:
        yield i
        i+=1

g=generator()
# i=iter(g)
# print(next(i))
# print(next(i))
# print(next(i))
for i in g:
    print(i)