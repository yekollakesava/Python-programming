class banking:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=0
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self):
        self.amount=int(input("enter the amount to withdraw: "))
        if self.amount > self.__balance:
            print("insufficent funds.!")
        else:
            self.__balance-=self.amount
            print("withdraw completed")
    
    def display(self):
        print(f"accountholder name:{self.name}\nbalance: {self.__balance}")

    def get_balance(self):
        return self.__balance

class savingsaccount(banking):
    def __init__(self, name, age,intrest):
        super().__init__(name, age)
        self.intrest=intrest
    def display(self):
        print(f"acount holder name:{self.name}\nbalance:{self.get_balance()}\nintrest rate:{self.intrest}")


class currentaccount(banking):
        def __init__(self, name, age):
            super().__init__(name, age)
        pass

h1=savingsaccount("ravi",25,"2%")
h1.deposit(1000)
h1.display()

print("-------current account-------")

h2 =currentaccount("ram",45)
h2.deposit(1000)
h2.deposit(500)
h2.display()
