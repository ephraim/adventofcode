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
        for s in subbags:
            m = re.match("(?P<amount>\d) (?P<subbag>[a-z ]+bag)s?", s)
            if not m:
                continue
            bag["subbags"][m.group("subbag")] = int(m.group("amount"))
        bags.append(bag)

    def addBag(result, bag, amount):
        if bag not in result.keys():
            result[bag] = amount
        else:
            result[bag] += amount
        return result

    def findBag(bags, needle):
        for b in bags:
            if needle == b["name"]:
                return b
        return None

    def findSubbags(bags, parent):
        if not parent or "subbags" not in parent:
            return []
        result = {}
        for s in parent["subbags"].keys():
            result = addBag(result, s, parent["subbags"][s])
            b = findBag(bags, s)
            if b:
                tmp = findSubbags(bags, b)
                for t in tmp.keys():
                    result = addBag(result, t, tmp[t] * parent["subbags"][s])
        return result

    count = 0
    b = findBag(bags, needle)
    if b:
        result = findSubbags(bags, b)
        for r in result.keys():
            print(r, result[r])
            count += result[r]

    print("Needed individual bags: %d"%count)
