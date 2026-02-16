def count_vowels(str):
    vowels="aeiouAEIOU"
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count

data=str(input("enter the string: "))
print(f"no of vowels in string is {count_vowels(data)}")