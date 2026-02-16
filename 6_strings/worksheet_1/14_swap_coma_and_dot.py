def swap(str):
    result=""
    for i in str:
        if i == ',':
            result+='.'
        elif i == '.':
            result+= ','
        else:
            result+=i
    return result

print(swap("123,456.789,"))