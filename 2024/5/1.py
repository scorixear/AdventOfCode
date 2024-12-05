import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    rules: dict[int, list[int]] = {}
    total = 0
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            ai, bi = int(a), int(b)
            if ai not in rules:
                rules[ai] = []
            rules[ai].append(bi)
        elif line.strip() != "":
            numbers = list(map(int, line.split(",")))
            middle = numbers[len(numbers) // 2]
            new_dict: dict[int, int] = {}
            for i, number in enumerate(numbers):
               new_dict[number] = i
            is_valid = True
            for i, number in enumerate(numbers):
                if number in rules:
                    afters = rules[number]
                    all_matched = True
                    for after in afters:
                        if after in new_dict:
                            if new_dict[after] < i:
                                all_matched = False
                                break
                    if not all_matched:
                        is_valid = False
                        break
            if is_valid:
                total += middle
    print(total)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
