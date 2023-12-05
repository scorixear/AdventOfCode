from collections import defaultdict
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    start = lines[-1]
    lines = lines[:-1]
    rules = defaultdict(list)
    for line in lines:
        if line == "":
            continue
        parts = line.split(" => ")
        molecule = parts[0]
        replacement = parts[1]
        rules[replacement].append(molecule)
    
    count = 0
    while start != "e":
        for replacement in rules:
            if replacement in start:
                start = start.replace(replacement, rules[replacement][0], 1)
                count += 1
                break
    print(count) 