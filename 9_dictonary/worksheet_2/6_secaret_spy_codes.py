codes = {'alpha': 'ok', 'beta': 'wait'}
new_labels = {'alpha': 'red', 'beta': 'blue'}

updated = {}

for old_key, value in codes.items():
    new_key = new_labels[old_key]
    updated[new_key] = value

print(updated)

 