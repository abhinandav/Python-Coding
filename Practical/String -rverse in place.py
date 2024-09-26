s='abhinand'

def reverse(s):
    n=len(s)-1
    i=0
    while i<n:
        s[i],s[n]=s[n],s[i]
        i+=1
        n-=1
    return s

print(reverse(s))