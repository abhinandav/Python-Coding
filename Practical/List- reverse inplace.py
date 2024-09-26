li=[1,2,3,4,5,6]

def reverse(li):
    n=len(li)-1
    i=0
    while i<n:
        li[i],li[n]=li[n],li[i]
        i+=1
        n-=1
    return li

print(reverse(li))