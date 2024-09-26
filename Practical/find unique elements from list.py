

def unique(li):
    new=[]
    for i in li:
        if i not in new:
            new.append(i)
    return new


print(unique([1,3,6,2,7,3,8,29]))

