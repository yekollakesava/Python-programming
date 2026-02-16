class banking_system:
    
    def __init__(self):
        self.balance=0
    def add_money(self,value):
        self.balance+=value
    def withdraw(self,value):
        self.balance -=value
    def display(self):
       return self.balance


bank=banking_system()
bank.add_money(1000)
bank.add_money(1000)
print(f"present balance: {bank.display()}")
bank.withdraw(500)
print(f"after withdrawing balance is:{bank.display()} ")

