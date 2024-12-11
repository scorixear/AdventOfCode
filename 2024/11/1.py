import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    stones = list(map(int, text.split(" ")))
    for _ in range(25):
        for i in range(len(stones)-1, -1, -1):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) % 2 == 0:
                str_stone = str(stones[i])
                stones[i] = int(str_stone[:len(str_stone) // 2])
                stones.insert(i + 1, int(str_stone[len(str_stone) // 2:]))
            else:
                stones[i] *= 2024
    # print(stones)    
    print(len(stones))


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
