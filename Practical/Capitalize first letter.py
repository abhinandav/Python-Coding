s='hai my name is abhinand'

def Capitalize(s):
    capital=True
    new=''
    for i in range(len(s)):
        if s[i] == ' ':
            new+=' '
            capital=True
        else:
            if capital:
                new+=s[i].upper()
                capital=False
            else:
                new+=s[i]
    return new
    

print(Capitalize(s))
        