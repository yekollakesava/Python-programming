voltage=float(input("enter voltage_reading: "))

if voltage>=3 and voltage<=3.35:
    print("normal")
elif voltage<3:
    print("under voltage")
else:
    print("high voltage")
    