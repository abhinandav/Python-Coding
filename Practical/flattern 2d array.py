

a=[1,[2,3],4,[5,6,[7,8]]]

def flattern(a):
    new=[]
    for i in a:
        if isinstance(i,list):
            new.extend(flattern(i))
        else:
            new.append(i)
    return new


print(flattern(a))
