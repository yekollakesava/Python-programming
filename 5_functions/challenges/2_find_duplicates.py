def find_duplicates(str):
    seen=set()
    duplicates=set()
    
    for num in str:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    print("duplicates: ",duplicates)

find_duplicates([4, 2, 4, 5, 2, 3, 4])
