n = input("Enter elements separated by comma: ")
data = tuple(n.split(","))

duplicates = () 

for item in data:
    if data.count(item) > 1 and item not in duplicates:
        duplicates += (item,)

print("Duplicate elements:", duplicates)

        
