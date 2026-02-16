def deepsum(lst):
    sum = 0
    for i in lst:
        if isinstance(i, list):
            sum += deepsum(i)
        else:
            sum += i
    return sum

list = [1, 2, [3, 4], 5, 6]
print(deepsum(list))
