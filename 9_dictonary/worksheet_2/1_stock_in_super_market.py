stock = {'apples': 14, 'bananas': 22, 'rice': 12}
quary=str(input("enter item you need to find: "))
if quary in stock:
    if stock[quary]>0:
        print("in stock")
    else:
        print("no stock")