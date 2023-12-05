import os, sys
from itertools import combinations


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    packages = [int(line) for line in lines]
    packages.sort(reverse=True)
    total_weight = sum(packages)
    target_weight = total_weight // 3

valid_first_packages = [[] for _ in range(len(packages))]

for i in range(1, len(packages)):
    found_packages = False
    for comb in combinations(packages, i):
        if sum(comb) == target_weight:
            quantum = 1
            for x in comb:
                quantum *= x
            valid_first_packages[i].append(quantum)
            found_packages = True
    if found_packages:
        break

for i in range(len(packages)):
    if valid_first_packages[i]:
        print(min(valid_first_packages[i]))
        break