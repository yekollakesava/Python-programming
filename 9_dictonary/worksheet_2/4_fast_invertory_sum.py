inventory = {'box': 30, 'crate': 22, 'pallet': 8}
sum=0
for i in inventory.values():
    sum+=i
print(f"total:{sum}")