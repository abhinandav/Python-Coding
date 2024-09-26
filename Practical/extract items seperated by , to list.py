

s='apple,banana,24,cherry,,fig'
def seperate(s):
    li=[]
    current=''
    for i in range(len(s)):
        if s[i]==',' and current!='':
            li.append(current)
            current=''
        else:
            if  i==len(s)-1:
                current+=s[i]
                li.append(current)
            else:
                current+=s[i]
    return li
            

print(seperate(s))
