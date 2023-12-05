import os, sys
import hashlib

def md5(input):
    return hashlib.md5(input.encode()).hexdigest()


with open(os.path.join(sys.path[0],"input.txt"), "r") as f:
    text = f.read().strip()
    
    current = 1
    while True:
        if md5(text + str(current)).startswith("00000"):
            break
        current += 1
    print(current)
