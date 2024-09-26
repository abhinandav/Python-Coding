def second(a):
    large=a[0]
    slarge=a[0]
    for i in range(1,len(a)):
        if a[i]>large:
            slarge=large
            large=a[i]
        elif a[i]>slarge and a[1]!=large:
            slarge=a[i]
    
    return slarge

print(second([1,2,3,4,5,6]))