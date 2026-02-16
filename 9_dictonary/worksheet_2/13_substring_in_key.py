d = {'hello': 1, 'world': 2, 'hell': 3}
substring = 'hell'
res=[]
for i in d:
    if substring in i:
        res.append(i)
print(res)