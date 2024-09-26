import random

def genrate():
    while True:
        otp=''.join(random.choice('123456789')for _ in range(0,6))
        if not any(char in otp for char in ['000','111','222','333','444','555','666','777','888','999']):
            return otp


print(genrate())
