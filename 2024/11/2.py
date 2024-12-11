from collections import defaultdict
import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    stones = list(map(int, text.split(" ")))
    stone_counter = dict()
    for stone in stones:
        if stone not in stone_counter:
            stone_counter[stone] = 1
        else:
            stone_counter[stone] += 1
    for _ in range(75):
        new_stones = dict()
        for stone, count in stone_counter.items():
            if stone == 0:
                set_or_increment(new_stones, 1, count)
            else:
                str_stone = str(stone)
                if len(str_stone) % 2 == 0:
                    set_or_increment(new_stones, int(str_stone[:len(str_stone) // 2]), count)
                    set_or_increment(new_stones, int(str_stone[len(str_stone) // 2:]), count)
                else:
                    set_or_increment(new_stones, stone * 2024, count)
        stone_counter = new_stones
    # print(stones)  
    total = 0
    for stone, count in stone_counter.items():
        total += count 
    print(total)

def set_or_increment(dictionary, key, count):
    if key not in dictionary:
        dictionary[key] = count
    else:
        dictionary[key] += count

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
