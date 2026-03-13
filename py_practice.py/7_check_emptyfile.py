with open("data.txt","r") as file:
    if file.read(1):
     print("file is not empty")
    else:
        print("file is empty")
