lst = ['a', 'b', 'c', 'd']

result = {}

for item in reversed(lst):
    result = {item: result}

print(result)
