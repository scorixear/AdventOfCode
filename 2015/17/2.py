from collections import defaultdict
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    containers = []
    for line in lines:
        containers.append(int(line))
    
    combinations = defaultdict(int)
    for i in range(2**len(containers)):
        total = 0
        container_count = 0
        for j in range(len(containers)):
            if i & (2**j):
                container_count += 1
                total += containers[j]
        if total == 150:
            combinations[container_count] += 1
    min_containers = min(combinations.keys())
    print(combinations[min_containers])
    
