n=int(input("enter number of elements to list: "))
fruits=[]
for i in range(n):
    fruit=str(input("enter data:"))
    fruits.append(fruit)
for i in range(len(fruits)):
    if fruits[i]=="banana":
        fruits[i]="dragonfruit"
print(fruits)
