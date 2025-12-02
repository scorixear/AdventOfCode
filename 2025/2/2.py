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
            for mod in range(2, len(strn) + 1):
                if len(strn) % mod == 0:
                    part_len = len(strn) // mod
                    parts = [
                        strn[i * part_len : (i + 1) * part_len] for i in range(mod)
                    ]
                    if all(p == parts[0] for p in parts):
                        total += n
                        break
    print(total)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
