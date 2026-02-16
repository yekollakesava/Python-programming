class shopping_cart:
    def __init__(self):
        self.items={}
    def additems(self,key,value):
        self.items[key]=value
    def removeitems(self,key):
        self.items.pop(key)
    def total(self):
        print(f"total bill={sum(self.items.values())}\nno of items ={len(self.items)}")
        print(dict(self.items))
    
a=shopping_cart()
a.additems("milk",50)
a.additems("creatine",50)
a.removeitems("creatine")
a.additems("strawberry",75)
a.additems("almond oil",2500)

a.total()