def count_characters(str):
    result=""
    output=[]
    for i in str:
        if i not in result:
            result=result+i
    
    for i in result:
        count=0
        for j in str:
            if i == j:
                count+=1
        output.append((i,count))

    return output

data=str(input("enter data: "))
print(count_characters(data))