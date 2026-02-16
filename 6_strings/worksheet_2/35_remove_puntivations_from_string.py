data=str(input("enter string: "))
result=""
for i in data:
    if i == '!' or i == ',' or i == '?': 
        continue
    else:
        result+=i
print(result)