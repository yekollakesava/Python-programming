with open("log.txt","r") as file:
    content=file.read()
content=content.splitlines()
with open("errorlog.txt","w")as f:
    for line in content:
        if "ERROR" in line:
            f.write(line)
            print(line)