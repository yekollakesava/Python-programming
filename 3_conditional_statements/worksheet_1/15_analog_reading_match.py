a1, a2 = map(int, input("Enter two analog readings: ").split(','))

print("Match" if abs(a1 - a2) <= 5 else "No Match")
