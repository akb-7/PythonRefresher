'''
file = open("fil.txt","r")
try:
    file.write("Hello")
finally:
    file.close()

# Another method

with open("fil.txt","r") as file:
    file.write("hello")

# this is similar to 
class File:
    def __init__(self,filename,method):
        print("Enter")
        self.file = open(filename,method)
    
    def __enter__(self):
        return self.file
    def __exit__(self,type,value,traceback):
        print("Exit")
        self.file.close()

with File("file.txt","w") as f:
    print("middle")
    f.write("hello")

'''

import contextlib
from contextlib import contextmanager
@contextmanager
def file(filename,method):
    print('enter')
    file = open(filename,method)
    yield file
    file.close()
    print('exit')

with file("text.txt","w") as f:
    f.write("hello")

