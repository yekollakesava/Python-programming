class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class employee(person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary=salary
    def display(self):
        print(f"name:{self.name} age:{self.age} salary: {self.salary}")
class manager(employee,person):
    pass

a=manager("ram",20,"10k")
a.display()    