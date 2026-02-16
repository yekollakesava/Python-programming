with open("error.txt","r")as file:
    content=file.read()

content=content.replace("you","this")
with open("error.txt","w")as file:
    file=file.write(content)
print(content)