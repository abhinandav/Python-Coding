a='apple,banana,25,,cherry,,'
# new=a.split(',')
# print(new)

def split(a):
    current=''
    li=[]
    for i in range(len(a)):
        if a[i]==',':
            if current!='':
                li.append(current)
            current=''
        else:
            current+=a[i]
            if i==len(a):
                li.append(current)

    return li

print(split(a))