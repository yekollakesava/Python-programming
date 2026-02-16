t1=(("red","yellow","green"),("pink","orange","black"),("white","blue"))
s=str(input("enter string you need to find: "))

for i in t1:
    if s in i[0] or i[1] or i[2]:
        print(True)
        break
    else:
        print(False)
