data=str(input("enter string: "))
data=set(data)
for i in data:
    if i != '0' and i!= '1':
        print("not a binary")
        break
    else:
        print("binary string")
        break