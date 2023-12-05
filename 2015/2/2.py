import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
    text = f.read().strip()
    lines = text.split("\n")
    result = 0
    for line in lines:
        dimensions = [int(x) for x in line.split("x")]
        dimensions.sort()
        result += 2*(dimensions[0] + dimensions[1]) + dimensions[0]*dimensions[1]*dimensions[2]
    print(result)