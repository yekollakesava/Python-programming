lst=[(1,2,3),(5,6,7),(8,9,0)]
result=[]
newvalue=100
for a in lst:
    new=a[:-1] + (newvalue,)
    result.append(new)

print(result)