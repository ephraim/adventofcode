import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    x = 3
    y = 1
    trees = 0

    while y < len(data):
        if x >= len(data[y]) - 1:
            x -= len(data[y]) - 1

        #print("(%d/%d) = %s"%(x,y, data[y][x]))
        if data[y][x] == "#":
            trees += 1

        x += 3
        y += 1

    print("trees: %d"%trees)
