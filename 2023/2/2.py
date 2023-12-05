import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    result = 0
    for line in lines:
        line = line.split(":")
        draws = line[1].split("; ")
        red, green, blue = 0, 0, 0
        for draw in draws:
            draw = draw.strip().split(", ")
            for color in draw:
                color = color.split(" ")
                ball = color[1]
                count = int(color[0])
                if ball == "red":
                    red = max(red, count)
                elif ball == "green":
                    green = max(green, count)
                elif ball == "blue":
                    blue = max(blue, count)
        result += red*green*blue
    print(result)