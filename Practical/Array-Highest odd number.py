def odd(a):
    h=float('-inf')
    for i in range(len(a)):
        if a[i]%2!=0 and a[i]>h:
            h=a[i]
    return h
print(odd([1,2,3,4,5,6,7,8]))


