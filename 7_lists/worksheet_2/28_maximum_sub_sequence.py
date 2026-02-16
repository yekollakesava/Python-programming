data=[2,-1,2,3,4,-5]
sum=0
for i in range(len(data)):
    if data[i]>=data[i-1]:
        sum+=data[i]
print(sum)