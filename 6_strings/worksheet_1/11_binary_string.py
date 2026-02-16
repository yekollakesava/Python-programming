def binarystring(s):
    for i in s:
        if i != '0' and i != '1':
            return "Not a binary string"
    return "Yes, it is a binary string"

s = "10001111"
print(binarystring(s))

    