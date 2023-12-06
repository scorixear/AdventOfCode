import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    t = int("".join(lines[0].split(":")[1].strip().split()))
    distance = int("".join(lines[1].split(":")[1].strip().split()))
    for i in range(1,t):
        if i * (t-i) > distance:
            print(t - i*2 + 1)
            break

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
