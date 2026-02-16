from itertools import permutations
list="abc"
result=permutations(list)

for i in result:
    print("".join(i))
