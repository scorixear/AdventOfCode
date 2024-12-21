from collections import deque
import os, sys
import time

N_PAD = {
    "7": [("8", ">"), ("4", "v")],
    "8": [("7", "<"), ("9", ">"), ("5", "v")],
    "9": [("8", "<"), ("6", "v")],
    "4": [("7", "^"), ("5", ">"), ("1", "v")],
    "5": [("2", "v"), ("8", "^"), ("6", ">"), ("4", "<")],
    "6": [("9", "^"), ("5", "<"), ("3", "v")],
    "1": [("4", "^"), ("2", ">")],
    "2": [("1", "<"), ("5", "^"), ("3", ">"), ("0", "v")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "0": [("2", "^"), ("A", ">")],
    "A": [("0", "<"), ("3", "^")],
}

D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "A": [("^", "<"), (">", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
}


def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        number = int(line[:-1])
        path_len = find_path_len(line, 2, True)
        total += number * path_len
    print(total)

def find_path_len(code: str, level: int, is_numpad: bool) -> int:
    if is_numpad:
        pad = N_PAD
    else:
        pad = D_PAD
    res = 0
    current = "A"
    for c in code:
        paths = bfs(current, c, pad)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(find_path_len(path, level - 1, False) for path in paths)
        current = c
    return res

def bfs(start: str, end: str, pad: dict[str, list[tuple[str, str]]]) -> list[str]:
    queue = deque([(start, [])])
    shortest = None
    res = []
    while queue:
        current, path = queue.popleft()
        if current == end:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for neighbour, direction in pad[current]:
            queue.append((neighbour, path + [direction]))
    return res

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
