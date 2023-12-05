import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    instructions = text.split(", ")
    right, up = 0, 0
    current_direction = 0
    for instruction in instructions:
        if instruction[0] == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4
        if current_direction == 0:
            up += int(instruction[1:])
        elif current_direction == 1:
            right += int(instruction[1:])
        elif current_direction == 2:
            up -= int(instruction[1:])
        else:
            right -= int(instruction[1:])
    print(abs(right) + abs(up))
    
