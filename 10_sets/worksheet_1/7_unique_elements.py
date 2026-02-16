old_hw = set(["math", "science", "art"])
new_hw =set(["math", "history", "science"])

for i in old_hw:
    if i not in new_hw:
        print(f"missing: {i}")
for i in new_hw:
    if i not in old_hw:
        print(f"newly added: {i}")
