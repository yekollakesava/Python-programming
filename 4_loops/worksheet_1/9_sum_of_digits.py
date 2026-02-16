num=int(input("enter the number: "))

while num>9:
    sum=0
    while num>0:
        sum=sum+num%10
        num=num//10
    num=sum

print(sum)
