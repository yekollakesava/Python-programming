words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat','ant']

groups={}

for word in words:
    key=''.join(sorted(word))
    groups[key]=groups.get(key,0)+1
res=max(groups.values())
print(res)
print(groups)