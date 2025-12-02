import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    ranges = [tuple(map(int, r.split("-"))) for r in lines[0].split(",")]
    total = 0
    for a, b in ranges:
        for n in range(a, b + 1):
            strn = str(n)
            if len(strn) % 2 == 0:
                left, right = strn[: len(strn) // 2], strn[len(strn) // 2 :]
                if left == right:
                    total += n
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
