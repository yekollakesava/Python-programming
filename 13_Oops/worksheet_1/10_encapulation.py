class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=None
    
    #setter
    def set_salary(self):
        return self._salary
    #getter
    def get_salary(self,value):
        self._salary=value
        return self._salary
        


emp=employee("raju","30")
print(emp.name,emp.age)
emp.set_salary()
print(emp.get_salary(10000))