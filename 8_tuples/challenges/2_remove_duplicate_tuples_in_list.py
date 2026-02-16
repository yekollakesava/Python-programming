lst=[(1,2),(3,4),(1,2)]
res=[]
for i in lst:
    if i not in res:
        res.append(i)
print(res)