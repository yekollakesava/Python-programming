lst = [(111, 2), (2, 10), (22, 11)]

def count_digits(l):
    return sum(len(str(x)) for x in l)

sorted_list = sorted(lst, key=count_digits)
print(sorted_list)
