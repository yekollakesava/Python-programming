def least_frequent_char(s):
  
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    min_freq = min(frequency.values())

    result = [char for char, count in frequency.items() if count == min_freq]

    return result, min_freq


text = "statistics"
chars, freq = least_frequent_char(text)

print(f"Least frequent character(s): {chars} (appears {freq} time)")

