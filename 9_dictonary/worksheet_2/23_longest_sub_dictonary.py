dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]

max_dict = dicts[0]

for d in dicts:
    if len(d) > len(max_dict):
        max_dict = d

print(max_dict)
