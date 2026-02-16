class typecheck:
    def __init__(self,data):
        self.data=data
    
    def type(self,data):
        print(f"{data}:{type(data)}")


A=typecheck(99)
A.type("king")
A.type(55)
A.type(55.99)       