voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (mA): "))

vol_safe = 3.0 <= voltage <= 3.3
cur_safe = 10 <= current <= 500

if vol_safe and cur_safe:
    print("Power OK")
elif not vol_safe and not cur_safe:
    print("Power Error")
elif not vol_safe:
    print("Voltage Error")
else:
    print("Current Error")
