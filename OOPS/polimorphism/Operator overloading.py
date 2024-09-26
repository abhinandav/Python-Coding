# class Add:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a+other.a
    

# obj1=Add(5)
# obj2=Add(10)

# print(obj1+obj2)




class UserAge:
    def __init__(self,age):
        self.age=age
    
    def __add__(self,other):
        return self.age+other.age
    

u1=UserAge(15)
u2=UserAge(15)

print(u1+u2)