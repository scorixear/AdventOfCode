import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    possible = 0
    for line in lines:
        line = line.split(":")
        game_id = int(line[0].replace("Game ",""))
        draws = line[1].split("; ")
        isPossible = True
        for draw in draws:
            draw = draw.strip().split(", ")
            for color in draw:
                color = color.split(" ")
                ball = color[1]
                count = int(color[0])
                if ball == "red" and count > 12:
                    isPossible = False
                    break
                elif ball == "green" and count > 13:
                    isPossible = False
                    break
                elif ball == "blue" and count > 14:
                    isPossible = False
                    break
            if not isPossible:
                break
        if isPossible:
            possible += game_id
    print(possible)