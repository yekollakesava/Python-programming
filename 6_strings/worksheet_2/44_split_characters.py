s = input("Enter the string: ")
n = int(input("Enter chunk size: "))

A = [s[i:i+n] for i in range(0, len(s), n)]
print("Chunks:", A)
