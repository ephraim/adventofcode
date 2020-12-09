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
        pos = parts[0].split("-")
        letter = parts[1].strip(":")
        if parts[2][int(pos[0]) - 1] == letter and parts[2][int(pos[1]) - 1] != letter:
            correct += 1
        elif parts[2][int(pos[0]) - 1] != letter and parts[2][int(pos[1]) - 1] == letter:
            correct += 1

    print("correct passwords: %d"%correct)
