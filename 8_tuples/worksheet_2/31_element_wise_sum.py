t1=(1,2,3,4)
t2=(3,5,2,1)
t3=(2,2,3,1)
res=[]
for i in range(len(t1)):
    total=t1[i]+t2[i]+t3[i]
    res.append(total)

print(tuple(res))
