def reverse_words(str):
    words=str.split()                 #split words
    reverse_words=words[::-1]         #reverselist
    return " ".join(reverse_words)      #join reversedlist


data=str(input("enter string: "))
print(reverse_words(data))
