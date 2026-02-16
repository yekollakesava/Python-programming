list=[1,2,3,4,5,6]
start=int(input("enter starting location of reversing: "))

list[start:]=list[start:][::-1]
print(list)