def words_frequency(text):
    words = text.split()    
    result = []

    unique = []
    for w in words:
        if w not in unique:
            unique.append(w)
            
    for w in unique:
        count = 0
        for x in words:
            if w == x:
                count += 1
        result.append((w, count))
    
    return result


data = input("Enter text: ")
print(words_frequency(data))


        