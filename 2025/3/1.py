import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        max_num = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                num = int(line[i] + line[j])
                max_num = max(max_num, num)
        total += max_num
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
