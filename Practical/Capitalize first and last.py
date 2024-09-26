s='hai my name is abhinand'

def Capitalize(s):
    capital=True
    new=''
    for i in range(len(s)):
        if s[i] == ' ':
            new+=' '
            capital=True
        
        elif capital:
            new+=s[i].upper()
            capital=False

        elif i==len(s)-1 or s[i+1]==' ':
            new+=s[i].upper()

        else:
            new+=s[i]
    return new
    

print(Capitalize(s))
        