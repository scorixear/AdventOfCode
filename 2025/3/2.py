import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        total += get_joltage(line, 12, "")
    print(total)


def get_joltage(line: str, length: int, current: str) -> int:
    if length > len(line):
        return 0
    if length == 0:
        return int(current)
    if length == 1:
        return int(current + max(line))

    for c in "987654321":
        if c in line:
            index = line.index(c)
            remaining = line[index + 1 :]
            result = get_joltage(remaining, length - 1, current + c)
            if result > 0:
                return result
    return 0


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
