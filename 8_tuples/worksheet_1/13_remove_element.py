n=input("enter elements to tuple seperated by coma: ")
data=tuple(n.split(","))

data=list(data)
data.remove('5')
data=tuple(data)
print(data)
