class calculate:
    def __init__(self,name,year_of_birth):
        self.name=name
        self.year_of_birth = year_of_birth
    def age(self):
        present_age = abs(self.year_of_birth - 2025)
        return f"{self.name} is {present_age} years old"

yob=int(input("enter the year of birth: "))

a=calculate("raj",yob)
print(a.age())