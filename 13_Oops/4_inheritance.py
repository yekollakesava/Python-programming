'''
INHERITANCE: The inheritance is an macheanism where one class use and utilize the attributes of another class

'''
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        return f"{self.name} is a designer...!"

class software_engineer(employee):
    def __init__(self, name, age,level):
        super().__init__(name, age)
        self.level=level
    def print_details(self):
        intro=f"my self {self.name} i am an {self.level} level software engineer"
        return intro
    def work(self):
        return f"{self.name} is a softwareEngineer...!"
class designer(employee):
    def work(self):
        return f"{self.name} is a designer...!"


emp=software_engineer("kesava",21,"junior")
print(emp.name,emp.age,emp.level)

emp2=designer("shiva",24)
print(emp2.name,emp2.age)

print(emp.print_details())
print(emp2.work())

#pholimorphism
employ=[software_engineer("kesava",21,"junior"),
        software_engineer("kesava",21,"junior"),
        designer("shiva",24)]

for e in employ:
   print(e.work())

