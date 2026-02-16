data="my_variable_python"
str=""
for i in data:
    if i=='_':
        continue
    else:
        str+=i
print(str)
