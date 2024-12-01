import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    pairs = [tuple(map(int, line.split("   "))) for line in lines]
    left = [pair[0] for pair in pairs]
    right = [pair[1] for pair in pairs]
    counted_right: dict[int, int] = {}
    for r in right:
        counted_right[r] = counted_right.get(r, 0) + 1
    count = 0
    for l in left:
        count += counted_right.get(l, 0) * l
    print(count)
    
    
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
