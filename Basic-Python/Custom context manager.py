
class FileOpen:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()


with FileOpen('eg.txt','w') as file:
    file.write('abhinand')


print(type(FileOpen))