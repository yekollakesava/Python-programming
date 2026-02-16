t = ((1, 2), (3, 4), (5, 6))
res=[]
for items in t:
    for x in items:
        res.append(x)
res=tuple(res)
print(res)