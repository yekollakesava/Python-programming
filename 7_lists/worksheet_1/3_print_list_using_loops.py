def forloop(data):
    for i in data:
        print(i)

def whileloop(data):
    i=0
    while i<len(data):
        print(data[i])
        i+=1


data=[1,2,3,4,5]
forloop(data)
whileloop(data)