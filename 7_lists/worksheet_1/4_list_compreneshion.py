def contain_A(data):
    list=[]
    for i in data:
        if 'a' in i:
            list.append(i)
    print(list)
                        
def replace_obj(data):
    for i in range(len(data)):
        if data[i] == "banana":
            data[i]="orange"
    print(data)



n=int(input("enter no of elelments "))
fruits=[]
for i in range(n):
    fruit=str(input("enter data: "))
    fruits.append(fruit)
print(fruits)
contain_A(fruits)
replace_obj(fruits)
