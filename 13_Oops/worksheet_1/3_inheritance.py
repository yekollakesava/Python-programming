class transportation_system:

    def __init__(self,name):
        self.name=name
   
    def mode(self,status):
        return f"{self.name} is moving...!"
    
class busses(transportation_system):
     def mode(self):
        return "buss is moving is moving...!"


data=busses("hi")
print(data.mode())
     

     #inheritance is a mecheanism where a class uses properties of another class