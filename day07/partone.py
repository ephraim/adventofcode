import os
import sys
import re

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    needle = "shiny gold bag"
    bags = []
    for d in data:
        m = re.match("^(?P<bag>.*bag)s\s*contain (?P<contain>.*)$", d)
        if not m:
            continue

        bag = { "name": m.group("bag").strip(), "subbags": {}}
        if m.group("contain") == "no other bags.":
            bags.append(bag)
            continue

        subbags = re.findall("(\d [^,\.]+)", m.group("contain"))
        #print(m.group("bag"), ": ", m.group("contain"), " => ", len(subbags))
        for s in subbags:
            m = re.match("(?P<amount>\d) (?P<subbag>[a-z ]+bag)s?", s)
            if not m:
                continue
            bag["subbags"][m.group("subbag")] = int(m.group("amount"))
        bags.append(bag)

    def find(bags, bag, n):
        if not bag["subbags"]:
            return False
        for s in bag["subbags"].keys():
            if s == n:
                return True

            subbag = None
            for b in bags:
                if s == b["name"]:
                    subbag = b
                    break
            if subbag:
                ret = find(bags, subbag, n)
                if ret:
                    return ret
            #else:
            #    print("subbag not found! %s"%s)
        return False

    result = []
    for b in bags:
        if find(bags, b, needle):
            result.append(b)

    print(len(result))
