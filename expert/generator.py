"""x = [i**2 for i in range(1000000000)]

for e in x:
    print(e)
"""
class Gen:
    def __init__(self,n):
        self.n = n
        self.last = 0
    
    def __next__(self):
        return self.next
    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last +=1
        return rv

g = Gen(100)
while True:
    try:
        print(next(g))
    except StopIteration:
        break

# Another method 

def generator(n):
    for i in range(n):
        yield i**2

g = generator(100) # this pauses the execution and whereas it make stop in previous 

for i in g:
    print(i)