num=int(input("enter the number"))

count=0
num=abs(num)
while num > 0:
    digit=num%10
    if digit==0:
        count=count+1
    num=num//10
print("no of times zero appear in number is =",count)