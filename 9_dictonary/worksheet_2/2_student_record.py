pets = {'Harry': 'owl', 'Ron': 'rat'}
quary=str(input("enter the name: "))

if quary in pets:
    print(pets[quary])
else:
    print("not found!")
