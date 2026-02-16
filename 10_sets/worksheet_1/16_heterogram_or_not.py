data=str(input("enter the data: "))
a=len(data)
data=set(data)
b=len(data)
if a==b:
    print("word is heterogram")
else:
    print("not a heterogram")
    