class engineering:
    institute="velammal institute"      #classattribute(similar to global variables)
    def __init__(self,name,gender,age):
       #instance attribute
        self.name=name
        self.gender=gender
        self.age=age    
    #instance_method
    def introduction(self):
        intro=(f"my name is {self.name} i am {self.age} years old")
        return intro

    def p_name(self):
        print(self.name)

    def add_college(self,college):
        print(f"my name is {self.name} i am {self.age} years old studying in {college}")

    def __str__(self):
        return f" name: {self.name} age:{self.age}"
      
#instance
stu1=engineering("ram","M","30")

print(stu1.name,stu1.gender,stu1.age)
print(stu1.institute)
print(stu1.introduction())    
stu1.p_name()
stu1.add_college(stu1.institute)
print(stu1)