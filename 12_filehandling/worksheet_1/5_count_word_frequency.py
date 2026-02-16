file=open("shiva.txt","w")
file.write("siva,siva,siva,ram,ram ,ram ,hanuman ,hanuman")
file.close()
dic={}
new_file=open("shiva.txt",'r').read()
#new_file.split(",")

words=[w.strip() for w in new_file.split(",")]
for word in words:
    dic[word]=words.count(word)

print(dic)