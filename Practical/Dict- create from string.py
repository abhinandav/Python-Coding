s='my name is abhinand'
li=s.split(' ')
di={}
for i in li:
    di[i]=len(i)
print(di)


dic={word:len(word) for word in s.split()}
print(dic)