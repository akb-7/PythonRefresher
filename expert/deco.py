
def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper
'''
def fun2():
    print("I am fun 2")

# Decorator 

# this thing can be done by 
fun3 = func(fun2)
fun3()


x = func(fun2)
print(x)
x()
'''


# like this

@func
def fun2():
    print("I am fun 2")

fun2()

# And if u have to pass argument for fun2() then the wrapper function
# to be changed as below
"""
def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        f(*args,**kwargs)
        print("Ended")
    return wrapper
"""
# And suppose if we need to written a function then we need to return the value

"""
def func(f):
    def wrapper(*args,**kwargs):
        print("Started")
        rv = f(*args,**kwargs) # store the return values
        print("Ended")
        return rv # return the return_value
    return wrapper
"""
# Creating a timer decorator 
from time import time,sleep

def timer(f):
    def wrapper(*args,**kwargs):
        start = time()
        rv = f(*args,**kwargs)
        total = time() - start
        print("Time:",total)
        return rv
    return wrapper

@timer
def sleep_two():
    sleep(2)    

sleep_two()    