people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]


soreted_people=sorted(people,key=lambda x:x['age'])
print(soreted_people)


def sort(dic,key):
    n=len(dic)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if dic[j][key]>dic[j+1][key]:
                dic[j],dic[i]=dic[i],dic[j]
                swapped=True
        if not swapped:
            break
    return dic


print(sort(people,'age'))