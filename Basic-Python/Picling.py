import pickle

shamal={'age':23,'place':'palakkad'}
abhi={'age':21,'place':'kannur'}

db={}
db['first']=shamal
db['second']=abhi

b=pickle.dumps(db)

print(b)

a=pickle.loads(b)
print(a)