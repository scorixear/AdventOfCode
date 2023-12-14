import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    
    balls = []
    stopper = [0] * len(lines[0])
    rows = len(lines)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                stopper[j] = i + 1
            elif c == "O":
                balls.append(rows - stopper[j])
                stopper[j] += 1
    print(sum(balls))
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
