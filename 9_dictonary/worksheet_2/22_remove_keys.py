d = {'sun': 1, 'sunny': 2, 'rain': 3}
substring = 'sun'
lst=[]
for i in d:
    if substring in i:
        lst.append(i)

for k in lst:
    d.pop(k)

print(d)