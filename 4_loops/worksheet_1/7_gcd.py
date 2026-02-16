a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# make numbers positive
a, b = abs(a), abs(b)

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("GCD =", a)
