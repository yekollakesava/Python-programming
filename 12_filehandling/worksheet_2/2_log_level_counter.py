with open("r.txt","r")as file:
    content=file.read()

words=content.split()
#content=content.splitlines()
#content=content.split(" ")
dic={}
for w in words :
    dic[w]=words.count(w)
print(dic)