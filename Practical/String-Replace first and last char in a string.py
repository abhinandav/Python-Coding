s='abhinand'
middle=s[1:-1]
print(s[-1]+middle+s[0])

a='Hello world'

def reverse(a):
    li=[]
    current=''
    for i in range(len(a)):
        if a[i]==' ':
            li.insert(0,current)
            current=''
        else:
            current+=a[i]
            if i==len(a)-1:
                li.insert(0,current)
    reversed=''
    for i in li:
        reversed+=i+" "
    return reversed

print(reverse(a))
    
    

