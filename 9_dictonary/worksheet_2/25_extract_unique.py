d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
lst=[]
for k in d.values():
    if k not in lst:
        lst.append(k)
print(lst)