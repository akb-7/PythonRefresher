# this is an script of python calculator
# create a file named calc.py
# then run the function and see
from mycalc import add,sub,mul,div

a,b = list(map(int,input("Enter the value of a and b ").split()))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))