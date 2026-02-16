def largest_number(data):
    large=data[0]
    for i in data:
        if i>large:
            large=i
    print(f"the largest element in list is {large}")




n=int(input("enter  no of elements: "))
data=[]
for i in range(n):
    a=int(input("enter the element: "))
    data.append(a)
largest_number(data)
