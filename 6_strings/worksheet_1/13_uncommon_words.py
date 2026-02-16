def notcommonwords(str,ptr):
    s1=str.split()
    p1=ptr.split()
    words = []
    for i in s1:
        if i not in p1:
            words.append(i)
    for i in p1:
        if i not in s1:
            words.append(i)
    return words

str="red yellow green"
ptr="red pink green"

print(notcommonwords(str,ptr))