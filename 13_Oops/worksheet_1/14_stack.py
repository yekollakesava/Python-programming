class stack:
    def __init__(self):
        self.items=[]
    
    def push (self,value):
        self.items.append(value)
   
    def Pop (self):
        if not self.items:
            return "stack is empty"
        else:
            return self.items.pop()
   
    def peek(self):
        return(self.items[-1])
   
    def is_empty(self):
        if(len(self.items)==0):
            return True
        else:
            return False
        
s=stack()
s.push(20)
s.push(10)
s.push(30)
print(s.items)
s.Pop()
print(s.items)
print(s.peek())