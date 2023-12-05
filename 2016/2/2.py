import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    buttons = [[None ,None, 1   ,None ,None ],
                [None ,2   ,3   ,4   ,None ],
                [5    ,6   ,7   ,8   ,9    ],
                [None ,"A" ,"B" ,"C" ,None ],
                [None ,None,"D" ,None ,None ]]
    x,y = 0,2
    code = ""
    for line in lines:
        for char in line:
            if char == "U":
                if y > 0 and buttons[y-1][x] != None:
                    y -= 1
            elif char == "D":
                if y < 4 and buttons[y+1][x] != None:
                    y += 1
            elif char == "L":
                if x > 0 and  buttons[y][x-1] != None:
                    x -= 1
            else:
                if x < 4 and buttons[y][x+1] != None:
                    x += 1
        code += str(buttons[y][x])
    print(code)
    