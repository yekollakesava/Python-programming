class shapes:

    def __init__(self,shape_name,radius,length,breadth):
        self.shape_name=shape_name
        self.radius=radius
        self.length=length
        self.breadth=breadth
    def drawing(self):
        return "drawing shapes"
    
class square(shapes):
    def drawing(self):
        return "drawing a square"
    
class circle(shapes):
    def drawing(self):
        return "drawing a circle"
   
s1=square("Square",0,5,6)
print(s1.drawing())
s2=circle("Circle",10,0,0)
print(s2.drawing())
