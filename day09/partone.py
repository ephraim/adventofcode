import os
import sys
import re

class Xmas():
    max_length = 25
    data = []

    def addNext(self, n):
        if len(self.data) < self.max_length:
            self.data.append(n)
            return True
        elif self.validate(n):
            self.data.append(n)
            self.data.pop(0)
            return True
        return False

    def validate(self, n):
        for i in range(0, self.max_length):
            for x in range(i, self.max_length):
                if (self.data[i] + self.data[x]) == n:
                    return True
        return False


if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    x = Xmas()
    for d in data:
        d = d.strip()
        if not x.addNext(int(d)):
            print(d)
            break
