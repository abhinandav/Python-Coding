a=[1,[2,3],4,[9,[20,45]],5]

def reverse(a):
    new=[]
    for i in range(len(a)-1,-1,-1):
        if isinstance(a[i],list):
            new.append(reverse(a[i]))
        else:
            new.append(a[i])
    return new

print(reverse(a))

def inReverse(a):
    a.reverse()
    for i in a:
        if isinstance(i,list):
            inReverse(i)
    return a

print(inReverse(a))