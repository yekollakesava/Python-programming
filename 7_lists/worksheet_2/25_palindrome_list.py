def palindrome(data):
    list=data
    list.reverse()
    if list == data:
        print("it is a palindrome")
    else:
        print("not a palindrome")



data=[1,1,2,1,1]
palindrome(data)