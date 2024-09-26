# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(6):
    for j in range(i):
        print(i, end=" ") 
    print(" ")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(6):
    for j in range(1,i+1):
        print(j, end=" ") 
    print(" ")

print()

# 11111
# 2222
# 333
# 44
# 5

for i in range(1,6):
    for j in range(6-i):
        print(i,end="")
    print()
print()

# 55555
# 4444
# 333
# 22
# 1


for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(6):
    for j in range(i,0,-1):
        print(j, end=" ") 
    print(" ")
print()

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

for i in range(5,0,-1):
    for j in range(i+1):
        print(j, end=" ") 
    print(" ")
print()




# *    *
# **   **
# ***  ***
# **** ****
# **********

for i in range(6):
    for j in range(i):
        print('*',end="")

    for k in range(5-i):
        print(' ',end='')

    for j in range(i):
        print('*',end="")

    print()