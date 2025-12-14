import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    fit = 0
    for line in lines:
        if "x" in line:
            dimensions, boxes = line.split(":")
            w, h = dimensions.split("x")
            area = int(w) // 3 * int(h) // 3

            totalboxes = sum(int(x) for x in boxes.split())
            if totalboxes <= area:
                fit += 1
    print(fit)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
