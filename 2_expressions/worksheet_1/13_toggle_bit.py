a=int(input("enter the number: "))
bit=int(input("enter the bit you need to toggle: "))

a=a^(1<<bit)

print(a)
