'''class aeroplane:
    def __init__(self):
        self.__speed=0
    
    def set_speed(self,speed):
        self.__speed=speed
    
    def get_speed(self):
        return self.__speed

a=aeroplane()
a.set_speed("300kmph")
print(a.get_speed())
'''

class marks:
    def __init__(self):
        self._c=None
        self._python=None
    
    def set_marks(self,c,python):
        self._c=c
        self._python=python

    def get_marks(self):
        return f"c: {self._c} python:{self._python}"
class Cmarks(marks):
    def __init__(self):
        super().__init__(self)
        pass

a=marks()
a.set_marks(90,60)
print(a.get_marks())