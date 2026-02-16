def removr_character(str,i):
    if i<0 or i>len(str):
        return str
    
    return str[:i] + str[i+1:]

data=str(input("enter the string: "))
i=int(input("enter index location: "))
result=removr_character(data,i)
print(f"after removing index value {result}")