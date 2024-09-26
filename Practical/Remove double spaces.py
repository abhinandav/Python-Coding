s='hai  my name   is    abhinand'

def remove_space(s):
    new=''
    space=False
    for i in s:
        if i!=' ':
            new+=i
            space=False
        elif not space:
            new+=' '
            space=True
    print(new)
        

remove_space(s)