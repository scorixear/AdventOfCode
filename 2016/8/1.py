import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    
    width = 50
    height = 6
    grid = [[0] * width for _ in range(height)]
    
    for line in lines:
        if line.startswith("rect"):
            x, y = map(int, line.split(" ")[1].split("x"))
            for i in range(y):
                for j in range(x):
                    grid[i][j] = 1
        elif line.startswith("rotate row"):
            values = line.split(" ")[2:]
            y = int(values[0].split("=")[1])
            amount = int(values[2])
            for _ in range(amount):
                grid[y] = [grid[y][-1]] + grid[y][:-1]
        elif line.startswith("rotate column"):
            values = line.split(" ")[2:]
            x = int(values[0].split("=")[1])
            amount = int(values[2])
            for _ in range(amount):
                last = grid[-1][x]
                for i in range(height-1, 0, -1):
                    grid[i][x] = grid[i-1][x]
                grid[0][x] = last
    print(sum(sum(row) for row in grid))
    for row in grid:
        print("".join("#" if x == 1 else "." for x in row))

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
