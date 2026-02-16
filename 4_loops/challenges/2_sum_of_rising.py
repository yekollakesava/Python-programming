for i in range(100,1000):
    temp=i
    sum=0
    pos=3
    while temp>0:
        digit=temp%10
        sum=sum+digit**pos
        temp=temp//10
        pos=pos-1
    if i == sum:
        print(i)
