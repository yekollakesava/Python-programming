def reverse_string(str):
    reversed=""
    for i in str:
        reversed=i+reversed
    return reversed

print(reverse_string("hello"))