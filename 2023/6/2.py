import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    t = int("".join(lines[0].split(":")[1].strip().split()))
    distance = int("".join(lines[1].split(":")[1].strip().split()))
    first_winning = t
    for i in range(t):
        if i * (t-i) > distance:
            first_winning = i
            break
    last_winning = 0
    for i in range(t-1, -1, -1):
        if i * (t-i) > distance:
            last_winning = i
            break
    print(last_winning - first_winning + 1)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
