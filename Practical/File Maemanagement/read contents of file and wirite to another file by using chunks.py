

def fileOP(source,dest,size=1024):
    with open(source,'rb') as file1:
         with open(dest,'wb') as file2:
                chunk=file1.read()
                if chunk:
                    file2.write(chunk)
    print('copied..')
            
              
              
source='eg.txt'
dest='eg2.txt'
fileOP(source,dest)
