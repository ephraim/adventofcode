import os
import sys


if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    def validate(p, ans):
        r = 0
        for a in ans.keys():
            if ans[a] == p:
                r += 1
        #print(p, ans, " => ", r)
        return r

    result = 0
    persons = 0
    answers = {}
    for d in data:
        d = d.strip("\n")
        if not d:
            result += validate(persons, answers)
            persons = 0
            answers = {}
            continue

        persons += 1
        for i in range(0, len(d)):
            if d[i] not in answers.keys():
                answers[d[i]] = 1
            else:
                answers[d[i]] += 1 


    result += validate(persons, answers)
    print(result)
