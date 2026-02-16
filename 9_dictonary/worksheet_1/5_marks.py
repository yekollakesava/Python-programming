n=int(input("enter how many kesy in dictonary: "))
data={}
for i in range(n):
    key=input("enter key: ")
    item=input("enter item: ")
    data[key]=item
print(data)