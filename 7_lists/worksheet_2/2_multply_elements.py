def mul_list(data):
    mul=1
    for i in data:
        mul*=i
    print(mul)


n=int(input("enter elements to list: "))
data=[]
for i in range(n):
    a=int(input("enter the data: "))
    data.append(a)
mul_list(data)