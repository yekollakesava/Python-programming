data=(("11","22"),("33","44"))
data=tuple(tuple(int(x) for x in group)for group in data)
print(data)