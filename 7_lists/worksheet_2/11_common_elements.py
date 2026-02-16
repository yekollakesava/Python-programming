def common_elements(data,data1):
    list=[]
    for i in data:
        if i in data1:
            list.append(i)
    print(list)

data=[1,2,3,4]
data1=[3,4,5,6]
common_elements(data,data1)