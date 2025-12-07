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

    queue = [start]
    visited = set()
    hit_spliters = 0
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if y + 1 >= height:
            continue
        if (x, y + 1) in splitter:
            hit_spliters += 1
            if x - 1 >= 0:
                queue.append((x - 1, y + 1))
            if x + 1 < width:
                queue.append((x + 1, y + 1))
        else:
            queue.append((x, y + 1))
    print(hit_spliters)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
