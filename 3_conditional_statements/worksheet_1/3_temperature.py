temp=float(input("enter voltage_reading: "))

if temp>=30 and temp<=33:
    print("normal")
elif temp<25:
    print("low temperature")
else:
    print("high temperature")
    