import random
import string

target = "abc"
attempts = 0

while True:
    attempts += 1
    s = ""
    for i in range(len(target)):
        s += random.choice(string.ascii_lowercase)

    if s == target:
        print("Generated:", s, "after", attempts, "attempts")
        break
