import itertools

a={1,2,3}
p=[]
for i in range(len(a)+1):
    p.extend(itertools.combinations(a,i))

print(p)
