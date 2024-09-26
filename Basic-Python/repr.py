# repr is used to get a string representation of object



print(repr('abhi'))  # op will be a string enclosed in " "   ---> "'abhi'",when we print normal string git give like "abhi"

ten=repr(10)

print(type(ten))   # op will be string

ten2=eval(ten)  # to get original
print(type(ten2))  # int