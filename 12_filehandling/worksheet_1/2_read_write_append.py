file=open("abc.txt",'w')
f1=open("ram.txt",'r')

for i in f1:
    file.writ(i)
file.close()
f1.close()