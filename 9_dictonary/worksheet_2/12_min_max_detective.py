valuables = {'ring': 5, 'necklace': 9, 'watch': 2}

min_item = max_item = list(valuables.keys())[0]

for item in valuables:
    if valuables[item] > valuables[max_item]:
        max_item = item
    if valuables[item] < valuables[min_item]:
        min_item = item

print(f"min: {min_item} max: {max_item}")

