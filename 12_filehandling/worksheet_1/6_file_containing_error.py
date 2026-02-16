content=open("error.txt","w")
content.write("error king kaakaka error233 preprocessor error translator error")
content.close()


content=open("error.txt","r").read()
data=content.split()
pattern="error"

file=open("r.txt",'w')
for i in data:
    if pattern in i:
        file.write(i+"\n")

file.close