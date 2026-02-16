for num in range(1000,2000):
    pro1=1
    pro2=1
    temp=num
    for i in range(2):
        digit=temp%10
        pro1=pro1*digit
        temp=temp//10
    for i in range(2):
        digit=temp%10
        pro2=pro2*digit
        temp=temp//10

    if pro1==pro2:
        print(num)


