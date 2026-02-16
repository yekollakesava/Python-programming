def find_all_index(s,sub):
    res=[]
    start=0
    while True:
        index=s.find(sub,start)
        if index == -1:
            break
        res.append(index)
        start=index+1
    return res


s=str(input("enter the string: "))
sub=str(input("enter the substring: "))

print(find_all_index(s,sub))
