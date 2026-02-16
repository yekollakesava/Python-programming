def palindrome_check(data):
    data1=data[::-1]
    if data==data1:
        return 1
    else:
        return 0


data=str(input("enter string: "))
if palindrome_check(data):
    print(True)
else:
    print("false")
