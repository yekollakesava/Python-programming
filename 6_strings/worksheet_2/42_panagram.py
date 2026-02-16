def is_panagram(str):
    str=str.lower()
    alphabets="abcdefghijklmnopqrstuvwxyx"

    for i in str:
        if i not in alphabets:
            return False
    return True

data=str(input("enter string: "))
if is_panagram(data):
    print("yes! string is panagram")
else:
    print("not a panagram")