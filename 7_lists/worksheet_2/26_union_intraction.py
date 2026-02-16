def common_elements(data,data1):
    list=[]
    list1=[]
    for i in data:
        if i in data1:
            list.append(i)
    for i in data:
        if i not in list1:
            list1.append(i)
    for i in data1:
        if i not in list1:
            list1.append(i)
            
    print(f"union: {list1}")
    print(f"common elements: {list}")

data=[1,2,3,4]
data1=[3,4,5,6]
common_elements(data,data1)