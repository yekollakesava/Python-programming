class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))   
print(issubclass(Animal, Dog))   
