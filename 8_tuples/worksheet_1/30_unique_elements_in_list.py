t=[(1,2),(3,4),(2,5)]
lst=[]
for item  in t:
    for i in item:
        lst.append(i)
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print(tuple(res)) 
