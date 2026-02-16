r1, r2, r3 = map(int, input("Enter three sensor readings: ").split(','))
threshold = 50

count_high = sum([r1 > threshold, r2 > threshold, r3 > threshold])
print("Majority High" if count_high >= 2 else "Majority Low")
