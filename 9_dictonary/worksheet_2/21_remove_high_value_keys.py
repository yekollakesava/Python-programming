d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10
remove_keys=[]

for k,v in d.items():
    if isinstance(v,int) and v > limit:
        remove_keys.append(k)

for k in remove_keys:
    d.pop(k)
print(d)
