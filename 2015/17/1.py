import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    containers = []
    for line in lines:
        containers.append(int(line))
    
    combinations = 0
    for i in range(2**len(containers)):
        total = 0
        for j in range(len(containers)):
            if i & (2**j):
                total += containers[j]
        if total == 150:
            combinations += 1
    print(combinations)
    
