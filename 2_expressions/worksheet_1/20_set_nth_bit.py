x=int(input("enter the number: "))

bit=int(input("enter the bit to set:"))

res= x | (1<<bit)

print("after setting: ",res)