lst=[(1,2),(-9,10),(5,4)]
result=[]
for item in lst:
    sum=0
    for x in item:
        sum+=x
    result.append(sum)
result=tuple(result)
print(result)