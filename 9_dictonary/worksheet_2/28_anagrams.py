words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']

anagrams = {}

for word in words:
    # sort the letters of the word to create a key
    key = ''.join(sorted(word))
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(word)

# get only the groups as a list
result = list(anagrams.values())
print(result)
