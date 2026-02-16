x=int(input("enter the number: "))
y=int(input("enter the number: "))
z=int(input("enter the number: "))

large = x if(x>y and x>z) else (y if(y>z) else z)

small = x if(x<y and x<z) else (y if(y<z) else z)

dif=large-small

print("difference is:",dif)





