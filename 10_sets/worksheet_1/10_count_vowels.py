msg = "hello world"
vowels = "aeiouAEIOU"
count = 0

for ch in msg:
    if ch in vowels:
        count += 1

print(count)