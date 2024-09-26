

s='my name is abhinand'

def change(s):
    new=''
    capitalize=True

    for i in range(len(s)):
        if   s[i]==' ':
             new+=s[i]
             capitalize=True
        elif capitalize==True:
                new+=chr(ord(s[i])-32)
                capitalize=False
        elif i==len(s)-1 or s[i+1]==" ":
             new+=chr(ord(s[i])-32)
        else:
             new+=s[i]

    return new


print(change(s))