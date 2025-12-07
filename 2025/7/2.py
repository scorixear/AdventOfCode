import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    splitter = []
    start = (0, 0)
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                splitter.append((x, y))
            elif c == "S":
                start = (x, y)

    dp = {}
    result = dfs(start[0], start[1], height, width, splitter, dp)
    print(result)


def dfs(x, y, height, width, splitter, dp) -> int:
    if (x, y) in dp:
        return dp[(x, y)]
    if y + 1 >= height:
        return 1
    total = 0
    if (x, y + 1) in splitter:
        if x - 1 >= 0:
            total += dfs(x - 1, y + 1, height, width, splitter, dp)
        if x + 1 < width:
            total += dfs(x + 1, y + 1, height, width, splitter, dp)
    else:
        total += dfs(x, y + 1, height, width, splitter, dp)
    dp[(x, y)] = total
    return total


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
