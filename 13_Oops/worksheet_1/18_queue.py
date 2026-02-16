class queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,value):
        self.data.append(value)
    def dequeue(self):
        self.data.pop(-1)
    def display(self):
        for i in range(len(self.data)):
            print(self.data[i])


a=queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.display()
a.dequeue()
print("after dequeuing")
a.display()

    