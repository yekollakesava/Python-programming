auction = {'lot1': 'coin', 'lot2': 'stamp', 'lot3': 'coin', 'lot4': 'comic'}
res=[]
for i in auction.values():
    if i not in res:
        res.append(i)
print(res)