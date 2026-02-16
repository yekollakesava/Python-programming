d = {'x': 100, 'y': 'hello', 'z': 200}
filtered = {}

for k, v in d.items():
    if isinstance(v, int):
        filtered[k] = v

print(filtered)