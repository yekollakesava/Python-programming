from abc import ABC,abstractmethod
class animal(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    def sleep(self):
        return "animal is sleeping"
class dog(animal):
    def __init__(self):
        super().__init__()
        pass
    def sound(self):
        print("bow bow..!")
    
class cat(animal):
    def __init__(self):
        super().__init__()
        pass
    def sound(self):
        print("meaw meaw..!")

a=dog()
a.sound()
print(a.sleep())

b=cat()
b.sound()
print(b.sleep())
