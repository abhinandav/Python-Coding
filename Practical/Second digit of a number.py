a=12345

def second(digit):
    if digit//10 < 10:
        return digit%10
    else:
        digit=second(digit//10)
        return digit
    
print(second(a))