num=int(input("enter the number"))
count=0
while num>0:
    count=count+1
    num//=10

print("no of digits is: ",count)