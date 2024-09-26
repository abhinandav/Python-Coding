

s='hai my name is abhinand i am from kannur'
new=s.split()
li=[x for x in new if x[0] in 'aeiouAEIOU']
print(li)