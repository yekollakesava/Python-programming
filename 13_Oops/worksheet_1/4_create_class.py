class schoolname:
    School_name="ravindra bharathi school"
    def __init__(self):
        pass
    
class student1(schoolname):
    pass
class student2(schoolname):
    pass


A = student1()
B = student2()
print(A.School_name , B.School_name)


