from difflib import get_close_matches

target = "apple"
words = ["apply", "apples", "ape", "maple"]

matches = get_close_matches(target, words, cutoff=0.5)
print("Close matches:", matches)