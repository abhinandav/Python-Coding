di={
    'abhinand':21,
    'shamal':24,
    'thomas':25,
    'salim':18
}

li=[v for v in di.values() if v>=20]
dic={(k,v) for k,v in di.items() if v>20}
print(li)
print(dic)