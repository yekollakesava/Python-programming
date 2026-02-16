words = ["education", "python", "sequoia"]
vowels="aeiouAEIOU"
res=[]
for word in words:
    count=0
    for ch in word:
        if ch in vowels:
            count+=1
    if count>=5:
        res.append(word)
print(res)

