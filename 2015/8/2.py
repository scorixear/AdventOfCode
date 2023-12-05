import os, sys

with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    result = 0
    for line in lines:
        result -= len(line)
        line = line[1:len(line)-1] # remove ""
        i = 0
        counter = 6
        while i < len(line):
            if line[i] == "\\":
                if line[i+1] != "x":
                    counter += 3
                    i += 2
                else:
                    counter += 4
                    i += 4
            else:
                i += 1
            counter += 1
        result += counter
    print(result)
    
    
