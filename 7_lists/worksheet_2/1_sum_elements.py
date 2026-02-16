def sum_list(data):
    sum=0
    for i in data:
        sum+=i
    print(sum)


n=int(input("enter elements to list: "))
data=[]
for i in range(n):
    a=int(input("enter the data: "))
    data.append(a)
sum_list(data)
