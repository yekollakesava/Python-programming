yesterday = [1, 2, 3, 4]
today = [1, 4, 2]

yesterday=set(yesterday)
today=set(today)

for i in yesterday:
    if i not in today:
        print(f"unique element is:{i}")