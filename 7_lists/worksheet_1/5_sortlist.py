n=int(input("enter number of values to list: "))
data=[]
for i in range(n):
    a=int(input("enter value: "))
    data.append(a)

data.sort()
print(data)

data.sort(reverse=True)
print(data)

new_list=data.copy()
print(new_list)