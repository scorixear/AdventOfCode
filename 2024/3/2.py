import os, sys
import time
import re

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    mul_re = r"(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    total = 0
    should_add = True
    for line in lines:
        all_patterns = re.findall(mul_re, line)
        for pattern in all_patterns:
            if pattern[0] == "don't()":
                should_add = False
                continue
            if pattern[0] == "do()":
                should_add = True
                continue
            if should_add:
                total += int(pattern[1]) * int(pattern[2])
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
