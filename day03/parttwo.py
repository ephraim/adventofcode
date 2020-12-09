import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    x = [ 1, 3, 5, 7, 1]
    y = 1
    trees = [0, 0, 0, 0, 0]
    twoY = False

    while y < len(data):
        for i in range(0, 5):
            if i == 4 and not twoY:
                twoY = not twoY
                continue
            else:
                twoY = not twoY

            if x[i] >= len(data[y]) - 1:
                x[i] -= len(data[y]) - 1

            #print("(%d/%d) = %s"%(x,y, data[y][x]))
            if data[y][x[i]] == "#":
                trees[i] += 1

            x[i] += (1+2*i) if i != 4 else 1
        y += 1

    print("result: %d"%(trees[0]*trees[1]*trees[2]*trees[3]*trees[4]))
