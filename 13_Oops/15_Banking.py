class bank:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=1000     #encaptulation
    def details(self):
        print(f"name:{self.name.upper()} age:{self.age}")
    def deposit(self,money):
        self.__balance+=money
        print("money deposited successfully..!")
    def withdraw(self,money):
        if self.__balance > 1000:
            self.__balance-=money
            print("money withdraw successfull")
        else:
            print("withdraw not possible \nlow minimum balance..!")
    def balance_enquary(self):
        print(f"Balance:{self.__balance}")

a=bank("raja saab",25)
a.details()
a.balance_enquary()
a.deposit(500)
a.balance_enquary()
a.withdraw(600)
a.balance_enquary()
a.withdraw(500)
a.balance_enquary()