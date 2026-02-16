import re
file=open("abc.txt",'w')
file.write("abc@123\nxyz@123\nkk@123")
file.close()

content=open("abc.txt","r").read()

pattern=r"\w+@\w+"
data=re.findall(pattern,content)
print(data)