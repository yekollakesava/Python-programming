def permutations(s):
    if len(s) == 0:
        return ['']  
    result = []
    for i in range(len(s)):
        for perm in permutations(s[:i] + s[i+1:]):
            result.append(s[i] + perm)
    return list(set(result))  


s = "aba"
print(permutations(s))