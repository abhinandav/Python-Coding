a=[1,2,3,4,5]
n1=lambda x:x**2
result=map(n1,a)
print(list(result))

from functools import reduce
n2=lambda a,b:a+b
print(n2(10,20))
result2=reduce(n2,a)
print(result2)