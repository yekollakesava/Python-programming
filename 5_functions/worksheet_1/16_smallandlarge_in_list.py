def find_small_and_large(list):
    large=small=list[1]
    for i in list:
        if small>i:
            small=i
        elif large<i:
            large=i
    return small,large

small,large=find_small_and_large([2,2,3,0,4,5,6])
print(f"small in list is {small}")
print(f"large in list is {large}")