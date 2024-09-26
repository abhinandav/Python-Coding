class CustomError(Exception):
    def __init__(self,message,code):
        self.message=message
        self.code=code
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} ( Error code : {self.code})"
    

def example(n):
    if n==0:
        raise CustomError('the given number is Zero',1111)
    

try:
    example(0)
except CustomError as e:
    print(e)