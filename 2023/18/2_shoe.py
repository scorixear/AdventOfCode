import os, sys
import time


def main():
    with open(os.path.join(sys.path[0],"simple.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    a = (0, 0)
    result = 0
    border = 0
    for line in lines:
        _, _, instructions = line.split()
        instructions = instructions[2: -1]
        length = instructions[:-1]
        direction = instructions[-1]
        length = int(length, base=16)

        # get next position
        if direction == "0":
            b = (a[0] + length, a[1])
        elif direction == "1":
            b = (a[0], a[1] + length)
        elif direction == "2":
            b = (a[0] - length, a[1])
        elif direction == "3":
            b = (a[0], a[1] - length)
        # add area of triangle to result
        result += (a[0] * b[1] - b[0] * a[1])
        # add border length
        border += length
        # prepare for next position
        a = b
    # if it didn't end where it started, we need to connect the last point to the first
    if a != (0,0):
        border += 2
    # = Area + border / 2 + 1
    print(abs(result)//2 + border // 2 + 1)
            
        
        
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:0.6f} seconds")