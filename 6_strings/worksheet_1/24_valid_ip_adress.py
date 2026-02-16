def adress(str):
    p1=str[:3]
    p2=str[3:6]
    p3=str[6:8]
    p4=str[8:]
    
    return f"{p1}.{p2}.{p3}.{p4}"


data=str(input("enter 11 digit number: "))
print(adress(data))