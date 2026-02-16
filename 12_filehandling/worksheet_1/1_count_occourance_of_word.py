file = open("ram.txt", 'r')
a = input("enter the word you need to count: ").lower()
count = 0

for line in file:
    words = line.lower().split()    # convert file words to lowercase
    for w in words:
        if w == a:
            count += 1

print(count)
file.close()
