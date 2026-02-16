def filter_strings(strings, substrings):
    result = []
    for s in strings:
        if all(sub in s for sub in substrings):
            result.append(s)
    return result

strings = ["applebanana", "apple", "banana", "applebananacherry"]
substrings = ["apple", "banana"]

filtered = filter_strings(strings, substrings)
print(filtered)
