data=[(2,5),(1,2),(4,4),(2,3),(2,1)]

def last_value(t):
    return t[1]

sorted_list=sorted(data,key=last_value)
print(sorted_list)