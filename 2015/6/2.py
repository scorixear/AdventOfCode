import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        if line.startswith("turn on "):
            line = line.replace("turn on ", "")
            line = line.replace(" through ", ",")
            line = line.split(",")
            for i in range(int(line[0]), int(line[2])+1):
                for j in range(int(line[1]), int(line[3])+1):
                    lights[i][j] += 1
        elif line.startswith("turn off "):
            line = line.replace("turn off ", "")
            line = line.replace(" through ", ",")
            line = line.split(",")
            for i in range(int(line[0]), int(line[2])+1):
                for j in range(int(line[1]), int(line[3])+1):
                    if lights[i][j] > 0:
                        lights[i][j] -= 1
        elif line.startswith("toggle "):
            line = line.replace("toggle ", "")
            line = line.replace(" through ", ",")
            line = line.split(",")
            for i in range(int(line[0]), int(line[2])+1):
                for j in range(int(line[1]), int(line[3])+1):
                    lights[i][j] += 2
    print(sum([sum(i) for i in lights]))