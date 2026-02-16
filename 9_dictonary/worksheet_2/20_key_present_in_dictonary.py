d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']
in_lst={}
for i in d:
    if i in lst:
        in_lst[i]=d[i]
print(in_lst)