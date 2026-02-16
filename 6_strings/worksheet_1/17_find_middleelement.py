def middle_element(s):
    length = len(s)

    if length % 2 == 0:
        mid = length // 2
        return s[mid - 1], s[mid]
    
    else:
        mid = length // 2
        return s[mid]


string = input("Enter the string: ")
print(f"The middle element in the string is {middle_element(string)}")
