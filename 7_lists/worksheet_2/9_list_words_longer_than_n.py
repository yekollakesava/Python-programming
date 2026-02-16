def list_longer_words(data):
    n=int(input("enter the minimum length of word: "))
    list=[]
    count=0
    for i in data:
        count=0
        for j in i:
            count=count+1
        if count>=n:
            list.append(i)
    print(list)



n=int(input("enter no of words in list: "))
data=[]
for i in range(n):
    a=str(input("enter the string: "))
    data.append(a)
list_longer_words(data)