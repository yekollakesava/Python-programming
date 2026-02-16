class arthematic_operations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return f"add: {self.num1+self.num2}"
    def sub(self):
        return f"sub: {self.num1-self.num2}"
    def multply(self):
        return f"multply: {self.num1*self.num2}"
    def divide(self):
        return f"divide: {self.num1 % self.num2}"
    
data=arthematic_operations(4,5)
print(data.add())
print(data.sub())
print(data.multply())
print(data.divide())
        