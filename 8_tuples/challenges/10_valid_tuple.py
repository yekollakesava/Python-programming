lst = [(None, None), (1, 2), (None, 3), (4, 5), (None, None)]
result = []

for tup in lst:
    if not all(v is None for v in tup):
        result.append(tup)

print(result)