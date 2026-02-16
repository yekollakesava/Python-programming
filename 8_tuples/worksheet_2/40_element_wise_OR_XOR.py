n=input("enter tuple seperated with coma: ")
m=input("enter tuple seperated with coma: ")

t1=tuple(map(int,n.split(",")))
t2=tuple(map(int,m.split(",")))

AND=[]
XOR=[]
for i in range(len(t1)):
    AND.append(t1[i] and t2[i])
    XOR.append(t1[i] ^ t2[i])

print(tuple(AND),tuple(XOR))
