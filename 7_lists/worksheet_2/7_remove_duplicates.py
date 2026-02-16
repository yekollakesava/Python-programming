def remove_duplicates(data):
    list=[]
    for i in data:
        if i not in list:
            list.append(i)
    print(list)



data=[1,2,3,5,2,1,3,4,1,9]
remove_duplicates(data)

