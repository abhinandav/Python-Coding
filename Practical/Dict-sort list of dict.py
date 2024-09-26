di=[
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 22},
    {'name': 'Dave', 'age': 30},
    {'name': 'Alice', 'age': 28}
]

sort=sorted(di,key=lambda x:x['name'])
print(sort)

