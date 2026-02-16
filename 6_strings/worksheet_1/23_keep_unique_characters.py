def keep_unique_characters(str):
    result=""
    for i in str:
        if i not in result:
            result += i
    return result

data=str(input("enter string: "))
print(keep_unique_characters(data))