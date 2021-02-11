def addNums(a=10,b=15):
    return a+b

#a , b = input("Enter the values of a,b ").split()
#a,b = int(a),int(b)
#print(addNums())
#print(addNums(a))
#print(addNums(a,b))

## Reading and writing the content on to the files

arr = ['Aakash','Aravind','Hegde']

with open("a.txt",'w') as a:
    for val in arr:
        a.writelines(val+"\n")


with open("a.txt","r") as b:
    arr = b.readlines()
    for val in arr:
        print(val,end="")

