def smallest_number(data):
    small=data[0]
    for i in data:
        if i<small:
            small=i
    print(f"the smallest element in list is {small}")




n=int(input("enter  no of elements: "))
data=[]
for i in range(n):
    a=int(input("enter the element: "))
    data.append(a)
smallest_number(data)
