spells = {'fireball': 5, 'healing': 10, 'curse': 2}
banned = ['curse', 'fireball']

for i in banned:
    spells.pop(i)

print(spells)