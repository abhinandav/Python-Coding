a=[1,2,3,4,5,6,7,8,9]
def reverse(a):
    n=len(a)-1
    i=0
    while i<n:
        a[i],a[n]=a[n],a[i]
        n-=1
        i+=1
    return a

print(reverse(a))

        