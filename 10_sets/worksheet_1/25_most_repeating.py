marbles = ["red", "blue", "red", "green", "blue", "red"]
maxcount=0
element=""
for i in marbles:
    count=0
    for l in range(len(marbles)):
        if i == marbles[l]:
            count+=1
    if count>maxcount:
        maxcount=count
        element=i
print(f"repeted:{count} times,element:{element}")