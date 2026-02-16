val = int(input("Enter a 16-bit value (hex e.g., 0xAAAA): "), 16)
parity = "Even" if bin(val).count('1') % 2 == 0 else "Odd"
print("Parity:", parity)
