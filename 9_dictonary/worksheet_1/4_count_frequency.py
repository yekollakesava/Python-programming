str=str(input("enter the string: "))
data={}
for i in str:
    key=i
    item=str.count(i)
    data[key]=item
print(data)