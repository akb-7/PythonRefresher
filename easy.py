# let us see the data types 

a = 1
b = "aakash"
c = 2.7 
d = [1,2,3,'a','b','c']
print(a,b,c,d,sep="\t")

# basic input output types

name = input("Enter the name, i will print it back ")
print(name,end="\n")

# now basic conditional statements 
# > < != == 

print("Aakash == aakash ? ","Aakash"=="aakash")

# now if else statements

a= int(input())
if a>0:
    print("a is greater than 0")
elif a==0:
    print("a is equal to 0")
else:
    print("a is less than 0")

# now let us see the for loops

print("Hurray i am going to print 5 numbers")
for i in range(0,5):
    print("X",sep=" ",end="\n")

# as an iterators
listq = ["Aakash","Aravind","hegde"]
for val in listq:
    print(val)

# now let us go to the data structures 

## list can be array or list { like we can use list as an array or even normal list}

objects = ["aakash","aravind",2,4.5]
print(objects)

# more string operations

stri = input("Enter something for strings ")

print(len(stri))
print(stri.upper())
print(stri.lower())
print(stri.split())

# slice operators
lis1 = [1,2,3,4,5,6,7,8,9,10]
print(lis1[1:4])
print(lis1[-1])
print(lis1[-1:])
print(lis1[:-1])
print(lis1[::-1])
