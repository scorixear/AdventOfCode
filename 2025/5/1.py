import os, sys
import time


def main():
    with open(os.path.join(sys.path[0], "input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    ranges = []
    ingredient_read = False
    total = 0
    for line in lines:
        if line == "":
            ingredient_read = True
            ranges = merge_ranges(ranges)
            continue
        if not ingredient_read:
            parts = line.split("-")
            sorted_insert(ranges, int(parts[0]), int(parts[1]))
        else:
            if find_range(ranges, int(line)):
                total += 1
    print(total)


def merge_ranges(ranges: list[tuple[int, int]]):
    result = []
    for start, end in ranges:
        if not result:
            result.append((start, end))
            continue
        last_start, last_end = result[-1]
        if start <= last_end:
            result[-1] = (min(last_start, start), max(last_end, end))
        else:
            result.append((start, end))
    return result


def sorted_insert(ranges: list[tuple[int, int]], start: int, inclusive_end: int):
    end = inclusive_end + 1
    for i, (s, _) in enumerate(ranges):
        if start < s:
            ranges.insert(i, (start, end))
            return
    ranges.append((start, end))


def find_range(ranges: list[tuple[int, int]], value: int) -> bool:
    for s, e in ranges:
        if s <= value < e:
            return True
    return False


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
