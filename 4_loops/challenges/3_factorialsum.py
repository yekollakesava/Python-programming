import math
for i in range(100,1000):
    temp=i
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+math.factorial(digit)
        temp=temp//10
    if i==sum:
        print(i)