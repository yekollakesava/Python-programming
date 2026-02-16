value = int(input("Enter a value (0-255): "))

if 0 <= value <= 63:
    print("Quadrant 1")
elif 64 <= value <= 127:
    print("Quadrant 2")
elif 128 <= value <= 191:
    print("Quadrant 3")
elif 192 <= value <= 255:
    print("Quadrant 4")
else:
    print("Invalid input")
