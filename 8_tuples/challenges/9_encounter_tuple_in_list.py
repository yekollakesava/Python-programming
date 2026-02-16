lst = [1, 2, 3, (4, 5), 6]
count=0
for i in lst:
    if not isinstance(i,tuple):
        count+=1
    else:
        break
print(count)