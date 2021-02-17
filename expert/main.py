# Dunder / Magic method & Pure Data Model
import inspect
'''
x = [1,2,3]
y = [4,5]

print(x+y)
print(len(x))
print(type(x))
'''

class Person:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        """
        String representation of the object
        """
        return f"Person({self.name})"
    
    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("Invalid Argument, must be integer")
        self.name *= x
    def __call__(self,y):
        print("Initialised the object with ",y)
    
    def __len__(self):
        return len(self.name)

p = Person("a")
print(p) #<__main__.Person instance at 0x7f62c9601830>
p*4
print(len(p))


from queue import Queue as q
import inspect

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
q = Queue()
print(q)

