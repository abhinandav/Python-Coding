s='hai my name is abhinand'

def Capitalize(s):
    capital=True
    li=s.split()
    new=''
    for word in li:
        length=len(word)
        if length%2==0 and length>2:
            mid1=length//2
            mid2=mid1+1
            newword=word[0].upper()+word[1:mid1]+word[mid1].upper()+word[mid2].upper()+word[mid2+1:-1]+word[-1].upper()
        else:
            mid1=length//2
            newword=word[0].upper()+word[1:mid1]+word[mid1].upper()+word[mid1+1:-1]+word[-1].upper()
        new+=newword+' '
    print(new)

print(Capitalize(s))
        

