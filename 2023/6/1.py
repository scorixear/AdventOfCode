import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    times = [int(x) for x in lines[0].split(":")[1].strip().split()]
    distances = [int(x) for x in lines[1].split(":")[1].strip().split()]
    result = 1
    for t, distance in zip(times, distances):
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
        #print(first_winning, last_winning, last_winning - first_winning + 1)
        result *= last_winning - first_winning + 1
    print(result)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
