data=str(input("enter string1: "))
data1=str(input("enter string2: "))
length=len(data)
count=0
for i in data:
        if i in data1:
                count+=1
if count == length:
        print("rotatary equilant")
else:
        print("not rotatary equivalent")

