import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    counter = 0
    for line in lines:
        levels = list(map(int, line.split(" ")))
        valid = True

        if not is_valid(levels):
            found_valid = False
            for i in range(0, len(levels)):
                if is_valid(levels[:i] + levels[i+1:]):
                    found_valid = True
                    break
            if not found_valid:
                valid = False
        if valid:
            counter += 1
    print(counter)

def is_valid(levels: list[int]):
    is_decreasing = None
    prev = levels[0]
    for i in range(1, len(levels)):
        diff = abs(levels[i] - prev)
        if is_decreasing is None:
            is_decreasing = levels[i] < prev
        if diff == 0 or diff > 3 or (is_decreasing and levels[i] > prev) or (not is_decreasing and levels[i] < prev):
            return False
        prev = levels[i]
    return True
    



if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
