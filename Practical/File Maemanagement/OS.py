import os

# if os.path.exists('example.txt'):
#     print('present')
# else:
#     print('not')

'''Remove'''
# if os.path.exists('eg.py'):
#     os.remove('eg.py')
# else:
#     print('not')

'''Rename'''

# os.rename('aa.py','eg.py')

'''crete and delete directory'''

# os.mkdir('abhinand')
# os.rmdir('abhinand')

import shutil

# shutil.copy('example.txt','eg.txt')
shutil.move('eg.txt','Basic/eg.txt')