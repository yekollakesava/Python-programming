nums = [11, 20, 12, 21, 3]
res=[]
sum=0
for i in nums:
    sum=0
    while i:
            digit=i%10
            sum+=digit
            i=i//10
    if sum not in res:
        res.append(sum)
print(res)
print(len(res))