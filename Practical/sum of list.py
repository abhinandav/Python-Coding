# sum of list

def Sum(li):
    if len(li)<1:
        return 0
    else:
        return li[0]+Sum(li[1:])
    

print(Sum([1,2,3,4,5]))