def count_occourance(data):
    sub=str(input("enter substring: "))
    a=data.count(sub)
    print(f"occourance of substring {a}")




n=int(input("enter no of elements to list: "))
data=[]
for i in range(n):
    a=str(input("enter string: "))
    data.append(a)
count_occourance(data)