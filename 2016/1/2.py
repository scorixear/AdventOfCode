import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    instructions = text.split(", ")
    x, y = 0, 0
    seen_locations = set((0,0))
    current_direction = 0
    for instruction in instructions:
        if instruction[0] == "R":
            current_direction = (current_direction + 1) % 4
        else:
            current_direction = (current_direction - 1) % 4
        if current_direction == 0:
            for i in range(int(instruction[1:])):
                y += 1
                if (x, y) in seen_locations:
                    print(abs(x) + abs(y))
                    break
                else:
                    seen_locations.add((x, y))
        elif current_direction == 1:
            for i in range(int(instruction[1:])):
                x += 1
                if (x, y) in seen_locations:
                    print(abs(x) + abs(y))
                    break
                else:
                    seen_locations.add((x, y))
        elif current_direction == 2:
            for i in range(int(instruction[1:])):
                y -= 1
                if (x, y) in seen_locations:
                    print(abs(x) + abs(y))
                    break
                else:
                    seen_locations.add((x, y))
        else:
            for i in range(int(instruction[1:])):
                x -= 1
                if (x, y) in seen_locations:
                    print(abs(x) + abs(y))
                    break
                else:
                    seen_locations.add((x, y))
    
