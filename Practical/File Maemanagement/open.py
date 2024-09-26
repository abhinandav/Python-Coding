# file=open('example.txt.','w')
# file.write('hello goodmorning')
# file.close()


# with open('example.txt.','w') as file:
#     file.write('how are you')


with open('example.txt.','w') as file:
    content=['abhi\n','jawhar\n','thomas\n']
    file.writelines(content)



# Read
# -----

# with open('example.txt.','r') as file:
    # content=file.read()
    # print(content)

# with open('example.txt.','r') as file:
#     for line in file:
#         print(line,end=" ")






