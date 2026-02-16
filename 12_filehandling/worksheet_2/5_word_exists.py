with open("error.txt","r") as file:
    content=file.read()

word=str(input("enter the word you need to find: "))
if word in content:
    print("yes..!")
else:
    print("no word not present")
    