def remove_all_occourances(data):
    list=[]
    for i in data:
        if i != 2:
            list.append(i)
    print(list)



data=[1,2,3,4,2,5,2,4,2,8,9,0]
remove_all_occourances(data)