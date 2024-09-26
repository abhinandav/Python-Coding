person={
    'name':'abhi','age':21,'place':'kannur'
}

def change(person):
    items = list(person.items())  
    print(items)
    person.clear()
    
    for key,value in items:
        person[value]=key
    return person

print(change(person))
