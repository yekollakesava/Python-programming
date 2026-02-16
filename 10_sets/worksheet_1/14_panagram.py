sentence = "The quick brown fox jumps over a lazy dog"
alpha="abcdefghijklmnopqrstuvwxyz"

sentence=set(sentence)
count=0
for ch in sentence:
    if ch in alpha:
        count+=1
if count>=25:
    print("string is panagram")
else:
    print("not a panagram")
#print(count)
#print(sentence)