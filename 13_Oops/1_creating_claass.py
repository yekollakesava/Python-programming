class softwareengineer:
    institute="ravindra bharathi"           #class attribute : can be utilized by any instance variable
    def __init__(self,name,age,level,salary):
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
#instance
se1=softwareengineer("kesava","20","junior","10k")
print(se1.salary,se1.name,se1.age,se1.level,se1.institute)
se2=softwareengineer("ram","25","junior","11k")
print(f"school:{se2.institute}")

