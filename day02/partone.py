import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    correct = 0
    for p in data:
        p = p.strip('\n')
        parts = p.split(" ")
        amount = parts[0].split("-")
        occurrences = parts[2].count(parts[1].strip(":"))
        if occurrences >= int(amount[0]) and occurrences <= int(amount[1]):
            correct += 1
    print("correct passwords: %d"%correct)
