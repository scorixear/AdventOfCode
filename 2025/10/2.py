import os, sys
import time
from itertools import product
from functools import cache
from collections import defaultdict


def main():
    with open(os.path.join(sys.path[0], "example.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    answ = 0
    for line in lines:
        parts = line.split(" ")
        indicators = [1 if c == "#" else 0 for c in parts[0][1:-1]]
        buttons = [[int(x) for x in p[1:-1].split(",")] for p in parts[1:-1]]
        joltages = tuple([int(x) for x in parts[-1][1:-1].split(",")])

        ops, patterns = {}, defaultdict(list)
        for pressed in product((0, 1), repeat=len(buttons)):
            jolt = [0] * len(joltages)
            for i, p in enumerate(pressed):
                for j in buttons[i]:
                    jolt[j] += p
            lights = tuple(x % 2 for x in jolt)
            ops[pressed] = jolt
            patterns[lights] += [pressed]

        @cache
        def try_buttons(target: list[int]):
            if all(x == 0 for x in target):
                return 0
            if any(x < 0 for x in target):
                return float("inf")

            total, lights = float("inf"), tuple(x % 2 for x in target)
            for pressed in patterns[lights]:
                diff = ops[pressed]
                new_target = tuple((b - a) // 2 for a, b in zip(diff, target))
                total = min(total, sum(pressed) + 2 * try_buttons(new_target))
            return total

        answ += try_buttons(joltages)
    print(answ)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
