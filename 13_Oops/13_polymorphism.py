class areaof:
    def __init__(self,length,breadth,radius):
        self.length=length
        self.breadth=breadth
        self.radius=radius
    def area(self):
        print(f"area: {self.length* self.breadth}")
class rectangle(areaof):
    pass
class circle(areaof):
    def area(self):
        a=2*3.14*self.radius*self.radius
        print(f"circle area:{a}")

c=circle(0,0,10)
c.area()

r=rectangle(5,5,0)
r.area()