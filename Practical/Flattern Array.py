a=[1,2,[4,6,8],[3,5]]

def flat(a):
    new=[]
    for i in a:
        if isinstance(i,list):
            new.extend(flat(i))
        else:
            new.append(i)
    return new

print(flat(a))
