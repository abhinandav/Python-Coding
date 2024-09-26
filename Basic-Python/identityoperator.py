a=[1,2,4]
print(id(a))

b=a
print(id(b))
c=[1,2,4]
print(id(c))

a,b=10,20
n=lambda a,b:a+b
print(n)