class Ages:
    def __init__(self,age):
        self._age=age
    
    @property
    def getAge(self):
        return self._age
    
    # @getAge.setter
    # def setAge(self,value):
    #     if value<18:
    #         raise ValueError(" you are minor")
    #     self._age=value

a=Ages(20)
print(a.getAge)
a.getAge=25
# print(a.getAge)

