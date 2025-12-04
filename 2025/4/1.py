import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    rolls = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "@":
                rolls.add((x, y))

    total = 0
    direction = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for roll in rolls:
        x, y = roll
        roll_count = 0
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (nx, ny) in rolls:
                roll_count += 1
        if roll_count < 4:
            total += 1
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
