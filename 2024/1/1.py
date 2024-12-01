import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    pairs = [tuple(map(int, line.split("   "))) for line in lines]
    left = [pair[0] for pair in pairs]
    right = [pair[1] for pair in pairs]
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    count = 0
    for i in range(len(sorted_left)):
        left = sorted_left[i]
        right = sorted_right[i]
        count += abs(left - right)
    print(count)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
