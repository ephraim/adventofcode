import os
import sys
import re

class Bootloader():
    accumulator = 0
    bootcode = []
    inp = 0

    def __init__(self, bootcode):
        for bc in bootcode:
            bc = bc.strip()
            cmd, param = bc.split(" ")
            self.bootcode.append({ "cmd": cmd, "param": param, "exec-count": 0 })

    def boot(self):
        ins = self.bootcode[self.inp]
        while True:
            ins["exec-count"] += 1
            if ins["exec-count"] == 2:
                print("exec count exit ...")
                break
            if ins["cmd"] == "nop":
                self.inp += 1
            elif ins["cmd"] == "acc":
                self.accumulator += int(ins["param"])
                self.inp += 1
            elif ins["cmd"] == "jmp":
                self.inp += int(ins["param"])
            if self.inp > len(self.bootcode):
                print("normal exit ...")
                break
            ins = self.bootcode[self.inp]
        return self.accumulator

if __name__ == "__main__":
    data = None
    wdir = os.path.dirname(sys.argv[0])
    with open(os.path.join(wdir, "input.txt")) as f:
        data = f.readlines()

    bl = Bootloader(data)
    print("Accumulator: ", bl.boot())
