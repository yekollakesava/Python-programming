class studentmarks:
    def __init__(self):
        pass
    def marks(self,c,python,cpp):
        self.c=c
        self.python=python
        self.cpp=cpp
    def average(self):
        total=self.c+self.python+self.cpp
        avg=total/3
        return avg
class nine(studentmarks):
    pass

a=studentmarks()
a.marks(20,20,20)
print(a.average())

b=nine()
b.marks(10,20,50)
print(b.average())