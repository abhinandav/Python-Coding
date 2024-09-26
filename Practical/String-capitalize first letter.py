s="my name is abhinand"

def Capital(s):
    capitalize=True
    result=''
    for i in s:
        if capitalize:
            i=chr(ord(i)-32)
            capitalize=False
        elif   i==' ':
            capitalize=True
        result+=i
    return result


print(Capital(s))