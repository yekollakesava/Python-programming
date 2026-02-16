class areaof:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return f"area:{self.length*self.breadth}"
    
class circle(areaof):
        def __init__(self, length, breadth,radius):
             super().__init__(length, breadth)  
             self.radius=radius

        def area(self):
            return f"area of circle:{3.14*(self.radius**2)}"
class triangle(areaof):
        def __init__(self, length, breadth,height,base):
             super().__init__(length, breadth)  
             self.height=height
             self.base=base

        def area(self):
            return f"area of circle:{1/2*self.base*self.height}"
        
class square(areaof):
     pass

tri=triangle(0,0,10,7)
Circle=circle(0,0,5)
Square=square(5,5)
print(tri.area())
print(Circle.area())
print(f"square {Square.area()} ")