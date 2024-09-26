di={'name': 'Alice', 'age': 28}


def greet(name,age):
    print(f"hello {name}, you are {age} year old")

greet(**di)

a=[1,2,3]
b=[*a]
print(b)
