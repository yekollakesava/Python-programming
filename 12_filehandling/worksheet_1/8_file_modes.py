with open("error.txt","a")as file:
    file.write("\nhi how are you")
with open("error.txt","r")as file:    
    content=file.read()
    print(content)
    print(file.mode)
    print(file.name)
    print(file.closed)