numbers=[1,2,9,3,0,4,5]
max=min=numbers[0]
res=set(numbers)
#max=min=next(iter(res))
for i in res:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f"max:{max} min:{min}")