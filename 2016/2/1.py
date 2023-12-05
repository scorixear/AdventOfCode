import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    buttons = [[1,2,3],[4,5,6],[7,8,9]]
    x,y = 1,1
    code = ""
    for line in lines:
        for char in line:
            if char == "U":
                y = max(0, y - 1)
            elif char == "D":
                y = min(2, y + 1)
            elif char == "L":
                x = max(0, x - 1)
            else:
                x = min(2, x + 1)
        code += str(buttons[y][x])
    print(code)
    