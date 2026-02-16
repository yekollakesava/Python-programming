n=int(input("enter number of elements in list: "))
fruits=[]
for i in range(n):
    fruit=str(input("enter list "))
    fruits.append(fruit)
print(f"before removing: {fruits}")
fruits.remove("banana")    
print(f"after removing: {fruits}")