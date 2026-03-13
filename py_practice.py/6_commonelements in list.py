list1=[1,2,3,4]
list2=[3,4,6,5]
res=[]
for i in list1:
    if i in list2:
        res.append(i)
print(res)