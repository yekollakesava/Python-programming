d = {'x': {'p': 1}, 'y': {'q': 2}}

flipped = {}

for outer_key, inner_dict in d.items():
    for inner_key, value in inner_dict.items():
        flipped[inner_key] = {outer_key: value}

print(flipped)
