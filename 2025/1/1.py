import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    curr = 50
    total = 0
    for line in lines:
        direction = line[0]
        value = int(line[1:])
        if direction == "L":
            curr = (curr - value) % 100
        elif direction == "R":
            curr = (curr + value) % 100
        if curr == 0:
            total += 1
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
