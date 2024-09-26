import copy

a=[[1,2,3],[4,5,6],[7,8,9]]
b=copy.copy(a)

print(a)
print(b)

b[0][1]='a'
print()
print(a)
print(b)


# shallow copy  creates the copy of a object but stores the reference to each element of the object

d=[[1,2,3],[4,5,6],[7,8,9]]
c=copy.deepcopy(d)
print()
print()

print(d)
print(c)

print('after edit')
c[0][1]='a'
print()

print(d)
print(c)

# deepcopy create copy of the object and elements of the objects


