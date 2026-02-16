class linked_list:
    def __init__(self):
        self.lst=[]

    def insert_element(self,value):
        self.lst.append(value)

    def delete_element(self, index):
        if 0 <= index < len(self.lst):
            self.lst.pop(index)
        else:
            print("Invalid index")

    def display(self):
        for i in range(len(self.lst)):
            print(self.lst[i])


a=linked_list()              
a.insert_element(10)
a.insert_element(20)
a.insert_element(30)
a.display()
print("after deleating")
a.delete_element(0)
a.display()