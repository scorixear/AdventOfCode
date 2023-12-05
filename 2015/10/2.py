from itertools import groupby
import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    for i in range(50):
        result = ""
        current = text[0]
        count = 1
        for i in range(1, len(text)):
            if text[i] == current:
                count += 1
            else:
                result += str(count) + current
                current = text[i]
                count = 1
        text = result + str(count) + current
    print(len(text))
    
