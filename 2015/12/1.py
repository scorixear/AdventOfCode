import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    ignore = False
    result = 0
    current = ""
    for c in text:
        if c == '"':
            ignore = not ignore
            if current != "":
                result += int(current)
                current = ""
        elif ignore:
            continue
        elif c.isdigit():
            current += c
        elif c == "-" and current == "":
            current += c
        else:
            if current != "":
                result += int(current)
                current = ""
    print(result)
            
    
