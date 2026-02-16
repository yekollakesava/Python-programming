orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
res={}
for i in orders:
    key=i
    item=orders.count(i)
    res[key]=item
print(res)