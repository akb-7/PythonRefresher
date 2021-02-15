
# map function

# Scenario: find a list of power of the values
## method 1 
li = [1,2,3,4,5]
def func(x):
    return x**x
newList = []
for x in li:
    newList.append(func(x))

print(newList)

## method 2

print(list(map(func,li)))

## method 3
print([func(x) for x in li]) # list comphrension

# Filter function

# Scenario: 

def add7(x):
    return x+7

def isOdd(x):
    return x%2!=0

a = [1,2,3,4,5]

print(list(filter(isOdd,a)))
# finding odd numbers after adding 7

print(list(filter(isOdd,list(map(add7,a)))))

# Lambda function {Single line fuction}

def fun(x):
    return x+5
fun2 = lambda x:x+5
print(fun(5),fun2(5))

# if we need to add function 5 to ll the values of the list

l = [1,2,3,4,5]
print(list(map(lambda x:x+5 ,l)))