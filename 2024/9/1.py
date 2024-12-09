import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    disk: list[int | None] = []
    mode = 0
    idx = 0
    for char in text:
        # disk
        if mode == 0:
            length = int(char)
            for _ in range(length):
                disk.append(idx)
            idx += 1
        # free space
        else:
            length = int(char)
            for _ in range(length):
                disk.append(None)
        mode ^= 1
    # print(disk)

    left = 0
    right = len(disk) - 1
    while True:
        # find the first free space
        for i in range(left, right + 1):
            if disk[i] is None:
                left = i
                break
        # find first disk
        for i in range(right, left - 1, -1):
            if disk[i] is not None:
                right = i
                break
        disk[right], disk[left] = disk[left], disk[right]
        left += 1
        right -= 1
        if left >= right:
            break
    # print(disk)
    total = 0
    for i, idx in enumerate(disk):
        if idx is None:
            break
        total += i * idx
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
