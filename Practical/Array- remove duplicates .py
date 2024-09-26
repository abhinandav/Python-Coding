a=[1,4,7,3,4,3,7,3,2,1]
def remove(a):
    i=0
    while i <len(a)-1:
        inner_index=i+1
        while inner_index<len(a):
            if a[i]==a[inner_index]:
                a.pop(inner_index)
            else:
                inner_index+=1
        i+=1
    return a

print(remove(a))
            