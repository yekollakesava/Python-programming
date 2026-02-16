def rotations(str):
    count=0
    for i in str:
        count+=1
    return count


data=str(input("enter string: "))
print(f"no of rotations to get orininal string is {rotations(data)}")