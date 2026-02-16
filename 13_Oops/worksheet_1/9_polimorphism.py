class shapes:

    def __init__(self,shape_name,radius,length,breadth):
        self.shape_name=shape_name
        self.radius=radius
        self.length=length
        self.breadth=breadth
    
class square(shapes):
    def area(self):
        a=self.length * self.breadth
        return f"area of square is {a}"
class circle(shapes):
    def area(self):
        a=2 * 3.14 *(self.radius)**2
        return f"area of circle is {a}"

s1=square("Square",0,5,6)
print(s1.area())
s2=circle("Circle",10,0,0)
print(s2.area())