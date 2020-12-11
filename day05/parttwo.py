import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    def nextRange(d, r):
        if d == "F" or d == "L": return (r[0], r[1] - ((r[1] - r[0] + 1) / 2))
        elif d == "B" or d == "R": return (r[0] + ((r[1] - r[0] + 1) / 2), r[1])

    seatIds = []
    for d in data:
        m = re.match("([FB]{7})([LR]{3})", d)
        if not m:
            print("regex not matches: ", d)
            continue

        row = (0, 127)
        for i in range(0, 7):
            row = nextRange(m.group(1)[i], row)

        if row[0] != row[1]:
            print(m.group(1))
            print(row)
            break
        row = row[0]
 
        col = (0, 7)
        for i in range(0, 3):
            col = nextRange(m.group(2)[i], col)

        if col[0] != col[1]:
            print(m.group(1))
            print(col)
            break
        col = col[0]

        seatIds.append(row * 8 + col)
    seatIds.sort()
    tmp = seatIds[0] - 1
    for i in range(0, len(seatIds)):
        if tmp + 1 != seatIds[i]:
            print("your seat ID: %d"%(tmp + 1))
            tmp = seatIds[i]
        else:
            tmp += 1
