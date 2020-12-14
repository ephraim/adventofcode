import os
import sys
import re

class Xmas():
    min_length = 2
    data = []
    currentSum = 0

    def __init__(self, invalidNr):
        self.invalidNr = invalidNr

    def addNext(self, n):
        self.data.append(n)
        self.currentSum += n

        while self.currentSum > self.invalidNr:
            n = self.data.pop(0)
            self.currentSum -= n
        if self.currentSum == self.invalidNr and len(self.data) > self.min_length:
            return True
        return False

    def getResult(self):
        min = -1
        max = 0
        for d in self.data:
            if min > d or min == -1:
                min = d
            if max < d:
                max = d
        return min + max

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    partoneNumber = 248131121
    x = Xmas(partoneNumber)
    for d in data:
        d = d.strip()
        if x.addNext(int(d)):
            print(x.getResult())
            break
