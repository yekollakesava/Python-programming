n=int(input("enter max range: "))
list=[]
for i in range(n):
    if i%2==0:
        list.append(i**2)
    else:
        list.append(i**3)
print(list)
