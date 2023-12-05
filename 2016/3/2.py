import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    count = 0
    for i in range(0, len(lines), 3):

        triangles = [[], [], []]
        for j in range(3):
            line = lines[i+j].split()
            for k in range(3):
                triangles[k].append(int(line[k]))
        for triangle in triangles:
            if triangle[0] + triangle[1] > triangle[2] and triangle[0] + triangle[2] > triangle[1] and triangle[1] + triangle[2] > triangle[0]:
                count += 1
    print(count)
        
