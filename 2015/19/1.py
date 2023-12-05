from collections import defaultdict
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    start = lines[-1]
    lines = lines[:-1]
    molecules = set()
    rules = defaultdict(list)
    for line in lines:
        if line == "":
            continue
        parts = line.split(" => ")
        molecule = parts[0]
        replacement = parts[1]
        rules[molecule].append(replacement)
    for i, c in enumerate(start):
        for replacement in rules[c]:
            if i == 0:
                molecules.add(replacement + start[i+1:])
            elif i == len(start) - 1:
                molecules.add(start[:i] + replacement)
            else:
                molecules.add(start[:i] + replacement + start[i+1:])
        if i < len(start) - 1:
            for replacement in rules[c + start[i+1]]:
                if i == 0:
                    molecules.add(replacement + start[i+2:])
                elif i == len(start) - 2:
                    molecules.add(start[:i] + replacement)
                else:
                    molecules.add(start[:i] + replacement + start[i+2:])
    print(len(molecules))
    
