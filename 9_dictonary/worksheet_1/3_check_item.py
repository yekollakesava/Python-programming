n=int(input("enter no of entries: "))
data={}
for i in range(n):
    key=input("enter key: ")
    item=input("enter item: ")
    data[key]=item
print(data)
print("fruit" in data)