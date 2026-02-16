data= [1, 2, 2, 3, 4, 4, 5, 6, 5]
list=[]
for i in data:
    if i not in list:
        list.append(i)
print(list)