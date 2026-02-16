d = {'m': 1, 'n': 2, 'o': 1}

grouped = {}

for key, value in d.items():
    if value not in grouped:
        grouped[value] = []
    grouped[value].append(key)
print(grouped)