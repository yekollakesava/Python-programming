a=int(input("enter data"))

if a>=1000:
    print("critical")
elif(a>=100 and a<=900):
    print("warning")
else:
    print("info: ",a)
    