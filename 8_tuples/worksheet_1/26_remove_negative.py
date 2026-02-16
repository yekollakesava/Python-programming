lst=[(1,2),(-9,10),(5,4)]

cleares_list=[t for t in lst if all(x>0 for x in t)]
print(cleares_list)
