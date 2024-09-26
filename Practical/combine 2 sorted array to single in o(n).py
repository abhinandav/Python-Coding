

a=[1,2,3,4,5]
b=[6,7,8,9,10]

def merge(a,b):
    i=j=0
    new=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            new.append(a[i])
            i+=1
        else:
            new.append(b[j])
            j+=1
    while i<len(a):
        new.append(a[i])
        i+=1

    while j<len(b):
        new.append(b[j])
        j+=1
    return new

print(merge(a,b))


