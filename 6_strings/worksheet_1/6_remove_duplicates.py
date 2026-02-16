def remove_duplicates(str):
    result=""
    for char in str:
        if char not in result:
            result=result+char

    return result

data=str(input("enter the string: "))
print(f"after removing duplicates {remove_duplicates(data)}")