t = ([1,2], [3,4], [5,6])
res=[]
for i in t:
    for j in range(len(i)):
        res.append(i[j])

print(tuple(res))

