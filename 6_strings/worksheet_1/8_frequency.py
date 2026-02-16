data=str(input("enter the string: "))

for char in data:
    if data.index(char)==data.find(char):
        count=0
        for c in data:
            if c in char:
                count+=1
        print(f"character:{char} frequency:{count}")