import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    houses = set()
    houses.add((0,0))
    curr_pos = (0,0)
    for c in text:
        if c == "^":
            curr_pos = (curr_pos[0], curr_pos[1] + 1)
        elif c == "v":
            curr_pos = (curr_pos[0], curr_pos[1] - 1)
        elif c == ">":
            curr_pos = (curr_pos[0] + 1, curr_pos[1])
        elif c == "<":
            curr_pos = (curr_pos[0] - 1, curr_pos[1])
        houses.add(curr_pos)
    print(len(houses))