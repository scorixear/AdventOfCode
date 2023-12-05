import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    count = 0
    for line in lines:
        line = line.split()
        if int(line[0]) + int(line[1]) > int(line[2]) and int(line[0]) + int(line[2]) > int(line[1]) and int(line[1]) + int(line[2]) > int(line[0]):
            count += 1
    print(count)
    
