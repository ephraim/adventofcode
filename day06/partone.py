import os
import sys


if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    def validate(ans):
        return len(ans)

    result = 0
    answers = {}
    for d in data:
        d = d.strip("\n")
        if not d:
            result += validate(answers)
            answers = {}
            continue

        for i in range(0, len(d)):
            answers[d[i]] = 1

    result += validate(answers)
    print(result)
