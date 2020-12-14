import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()
    
    def validate_byr(v):
        return int(v[0]) >= 1920 and int(v[0]) <= 2002

    def validate_iyr(v):
        return int(v[0]) >= 2010 and int(v[0]) <= 2020

    def validate_eyr(v):
        return int(v[0]) >= 2020 and int(v[0]) <= 2030

    def validate_hgt(v):
        return ((v[1] == "cm" and int(v[0]) >= 150 and int(v[0]) <= 193) or
                (v[1] == "in" and int(v[0]) >= 59 and int(v[0]) <= 76))

    def validate_ecl(v):
        return v[0] in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ]

    def validate(pp):
        needed = {
                "byr": { "p": "^(\d{4})$", "f": validate_byr },
                "iyr": { "p": "^(\d{4})$", "f": validate_iyr },
                "eyr": { "p": "^(\d{4})$", "f": validate_eyr },
                "hgt": { "p": "^(\d+)(cm|in)$", "f": validate_hgt  },
                "hcl": { "p": "^#[0-9a-f]{6}$", "f": None },
                "ecl": { "p": "(.*)", "f": validate_ecl },
                "pid": { "p": "^(\d{9})$", "f": None }
            }
        valid = True
        for k in needed.keys():
            if k not in pp.keys():
                valid = False
                break
            else:
                m = re.match(needed[k]["p"], pp[k])
                if not m or (needed[k]["f"] and not needed[k]["f"](m.groups())):
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
