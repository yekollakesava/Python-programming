n=input("enter elements seoerated by coma: ")
data=tuple(n.split(","))
res=[]
for i in data:
    if i not in res:
        res.append(i)
print(tuple(res))
