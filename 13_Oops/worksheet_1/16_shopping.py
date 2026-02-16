class shopping_cart:
    sum=0
    def __init__(self):
        self.cart={}
    def add_in_cart(self,key,value):
        self.cart[key]=value
        shopping_cart.sum+=value
    def display(self):
        print(self.cart)

c1=shopping_cart()
c1.add_in_cart("pens",5*20)
c1.add_in_cart("books",2*200)
c1.display()
print(c1.sum)
        