
# 1  
# 2 3 4  
# 5 6 7 8 9

count=0
for i in range(6):
    if i%2!=0:
        for j in range(i):
            count+=1
            print(count, end=" ") 
        print(" ")
print()

# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1  
# 1 2 3 4 5 4 3 2 1

for i in range(7):
    for j in range(1,i-1):
        print(j, end=" ") 
    for j in range(i-1,0,-1):
        print(j, end=" ") 
    print(" ")
print()





def print_pattern(n):
  for i in range(n, 0, -1):
    for j in range(1, i + 1):
      print(j, end="")
    print(" " * (2 * (n - i)), end="")
    for j in range(i, 0, -1):
      print(j, end="")
    print()

n = 5
print_pattern(n)
    

print()
print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print(" "*(2*(5-i)),end="") 
#     for j in range(i,0,-1):
#         print(j, end="") 
#     print(" ")
# print()


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print(" "*(2*(5-i)),end="") 

    for j in range(6-i,6):
        print(j, end="") 
    print()
print()



for i in range(5):
   print(" "*i,end="")
   for j in range(5-i):
      print("*",end=" ")
   print()
    
    
    






