# entering into the final stages
# try catch

a = input("Please enter any integer value ")
try: # this block is for there may error occur
    a = int(a)
except Exception:  # if the error occured we should do this block
    print("Entered values is not integer")
else: # if the try condition fails it enters here and execute here
    print("Else block")
finally: # this will execute always used to close a file or close a socket kind of stuff
    print("Finally block")

# lets move on to next final stage global and local variables

def add(a,b):
    ans = a+b
    print(ans)

a,b = (2,3)
add(a,b)
# print(ans) # this will show an error because ans is local variable for add function

# now if we denote it as global

ans = 0
def addd(a,b):
    global ans
    ans = a+b
addd(a,b)
print(f"The global value of ans {ans}")


# finally intro to class and objects

class Decoration():
    def __init__(self,dec):
        self.dec = dec
    def print(self):
        print(self.dec*5)

obj = Decoration("*")
obj.print()