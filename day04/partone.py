import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    def validate(pp):
        needed = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]
        valid = True
        for k in needed:
            if k not in pp.keys():
                valid = False
                break

        return valid

    passports = 0
    pp = {}
    for d in data:
        d = d.strip("\n")
        if not d:
            if validate(pp):
                passports += 1
            pp = {}
            continue

        for i in d.split(" "):
            tmp = i.split(":")
            pp[tmp[0]] = tmp[1]

    if validate(pp):
        passports += 1
    print("valid passports: %d"%passports)
