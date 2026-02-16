lst=[(1,2,3),(4,5),(6,7,8)]
res=[]
for t in lst:
    if len(t)>=3:
        res.append(t)
print(res)