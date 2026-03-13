str="a1b2c3"
digits="1234567890"
count=0
sum=0
for i in str:
    if i in digits:
        sum+=int(i)
        count+=1
average=sum/count
print(f"sum:{sum} average:{average}")  