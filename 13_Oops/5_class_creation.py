class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"my self {self.name} i am {self.age} old i am a designer")
class software(employee):
    def __init__(self, name, age,level):
        super().__init__(name, age)
        self.level=level
    def details(self):
        print(f"my self {self.name} i am {self.age} old i am {self.level} level developer")
class designer(employee):
    def __init__(self, name, age):
        super().__init__(name, age)
    def details(self):
        print(f"my self {self.name} i am {self.age} old i am a designer.123")


emp=software("ram",25,"junior")
emp.details()
emp1=designer("ravi",35)
emp1.details()