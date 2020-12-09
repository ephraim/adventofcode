import os
import sys


if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()
    if data:
        for i in range(0, len(data)):
            for x in range(i, len(data)):
                for y in range(x, len(data)):
                    if int(data[i]) + int(data[x]) + int(data[y]) == 2020:
                        print("%d * %d * %d = %d"%(int(data[i]), int(data[x]), int(data[y]), int(data[i]) * int(data[x]) * int(data[y])))
                        sys.exit()
