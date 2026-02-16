n=input("enter element to tuple seperatedby coma: ")
data=tuple(n.split(","))
for i in range(len(data)):
    print(data[i])