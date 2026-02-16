class engine:
    def __init__(self):
        self.horsepower="120hp"
class car(engine):
    pass
    def display(self):
        print(f"horsepower:{self.horsepower}")

a=car()
a.display()