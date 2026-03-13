text="The quick brown fox jumps over lazy dog"
text=text.split(" ")
words=["dog","fox","horse"]
for i in range(len(words)):
    if words[i] in text:
        print(f"{words[i]} found")
    else:
         print(f"{words[i]} notfound")