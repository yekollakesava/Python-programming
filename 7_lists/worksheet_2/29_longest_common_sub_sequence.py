def longest_common_subsequence(a, b):
    result = []
    pos = 0  

    for x in a:
        for i in range(pos, len(b)):
            if x == b[i]:
                result.append(x)
                pos = i + 1 
                break

    return result

list1 = [1, 3, 4, 1, 2, 3, 4, 1]
list2 = [3, 4, 1, 2, 1, 3]

print(longest_common_subsequence(list1, list2))