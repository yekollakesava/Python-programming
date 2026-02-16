file=open("ram.txt",'w')
file.write("i love python programming")
file.close()

file=open("ram.txt",'r')
content=file.read()
print(content)
file.close()