class banking:                                                        #class: class is a an blue print for creating objects
    def __init__(self,name,age):                                      
        self.name=name
        self.age=age
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self):
        self.amount=int(input("enter the amount you need to withdraw: "))
        if self.balance < self.amount:
            print("in sufficient funds\nenter valid amount")
        else:
            self.balance-=self.amount
            print(f"after withdrawing amount your account balance is {self.balance}")
    def checkbalance(self):
        print(f"balance:{self.balance}")
    def info(self):
        print(f"account holder name: {self.name}\nage: {self.age}")
class unionbank(banking):
    pass

a=(banking)("ram",30)           #object : object is an instance of class
a.deposit(1000)
a.deposit(500)
a.checkbalance()
a.withdraw()


b=(unionbank)("ravi",40)
b.info()







        