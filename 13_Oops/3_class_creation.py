class employee:
    compeny="bitsilica" #class attribute
    def __init__(self,name,age,role):
        self.name=name
        self.age=age        #instanceattribute
        self.role=role
    
    #instance method
    def __str__(self):
        introduction = f"my name is {self.name} i am working in {self.compeny} as {self.role}"
        return introduction
    def add_language(self,language):
        return f"{self.name} love coading in {language} programming language"

emp=employee("keshav redddy","23","embedded engineer") #instance
print(emp)
emp.add_language("c")
print(emp.add_language("c"))