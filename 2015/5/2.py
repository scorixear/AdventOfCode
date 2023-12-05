import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    count = 0
    for line in lines:
        check_double = False
        check_repeat = False
        for i in range(0, len(line)-1):
            if line[i] + line[i+1] in line[i+2:]:
                check_double = True
        for i in range(0, len(line)-2):
            if line[i] == line[i+2]:
                check_repeat = True
        if check_double and check_repeat:
            count += 1
       
    print(count)
    
