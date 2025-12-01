import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    curr = 50
    total = 0
    for line in lines:
        direction = -1 if line[0] == "L" else 1
        value = int(line[1:])
        next_curr = curr + direction * value
        # did we cross zero?
        if next_curr <= 0:
            # count how many times we crossed zero
            total += abs(next_curr // 100)
            # if we landed on zero exactly, add one more
            if next_curr % 100 == 0:
                total += 1
            # if we already were at zero, we need to subtract one
            # to avoid double counting
            if curr == 0:
                total -= 1
        elif next_curr >= 100:
            total += next_curr // 100
        curr = next_curr % 100
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
