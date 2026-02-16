friends_colors = [
  ["red", "blue"],
  ["green", "red"],
  ["yellow", "blue"]
]
res=[]
for l in friends_colors:
    for i in l:
        if i not in res:
                res.append(i)

print(set(res))
    