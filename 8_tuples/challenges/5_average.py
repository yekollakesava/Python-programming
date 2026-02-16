t = ((10, 10, 10, 12), 
     (30, 45, 56, 45), 
     (81, 80, 39, 32), 
     (1, 2, 3, 4))

rows = len(t)
cols = len(t[0])

result = []

for c in range(cols):
    total = 0
    for r in range(rows):
        total += t[r][c]
    result.append(total / rows)

print(result)


