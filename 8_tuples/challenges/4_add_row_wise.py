t=((1,2,3),(4,5,6),(5,6,7))
res=[]
for i in t:
    sum=0
    for j in range(len(i)):
        sum+=i[j]
    res.append(sum)
print(res)

