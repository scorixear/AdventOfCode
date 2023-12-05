import os, sys

with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
    input = f.read().strip()
    counter = 0
    for c in input:
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
    print(counter)