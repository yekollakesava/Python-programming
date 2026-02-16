x=int(input("enter the number: "))
shifts=int(input("enter no of shifts: "))

left=(x << shifts) or (x >>(32-shifts))

print("after rotating number:",left)