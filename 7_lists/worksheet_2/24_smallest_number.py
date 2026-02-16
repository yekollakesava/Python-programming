n=int(input("enter number of elements in array: "))
data=[]
for i in range(n):
    a=int(input("enter elements: "))
    data.append(a)
print(f"minimun element in list is {min(data)}")