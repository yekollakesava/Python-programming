def find_index(data,word):
    position=data.find(word)
    return position

data=str(input("enter the string: "))
word=str(input("enter word you need to find index: "))
print(f"word at index location {find_index(data,word)}")
