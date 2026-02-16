class notebook:
    def __init__(self,name):
        self.name=name
        
    def meeting_notes(self,text):
            return f"Mr {self.name} has{text}"
        
    def grossery_list(self,text):
            return f"gorssarylist:{text}"

book=notebook("keshav reddy")
print(book.meeting_notes("to meet mr shiva at 12'O clock"))
print(book.grossery_list("apple,banana,brinjal"))

        