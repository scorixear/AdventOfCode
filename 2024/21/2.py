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
    dp = {}
    for line in lines:
        number = int(line[:-1])
        # find the shortest path
        path_len = find_path_len(line, 25, True, dp)
        total += number * path_len
    print(total)

def find_path_len(code: str, level: int, is_numpad: bool, dp) -> int:
    if (code, level, is_numpad) in dp:
        return dp[(code, level, is_numpad)]
    # if we are using numpad, use N_PAD, otherwise use D_PAD
    if is_numpad:
        pad = N_PAD
    else:
        pad = D_PAD
    res = 0
    # we start at "A"
    current = "A"
    # for each character in the code
    for c in code:
        # find all possible paths to reach the character
        paths = bfs(current, c, pad)
        # if we are at the last level, add the minimum path length
        if level == 0:
            res += min(map(len, paths))
        # otherwise, add the minimum path length of the next level
        else:
            res += min(find_path_len(path, level - 1, False, dp) for path in paths)
        current = c
    dp[(code, level, is_numpad)] = res
    return res

def bfs(start: str, end: str, pad: dict[str, list[tuple[str, str]]]) -> list[str]:
    # start from the starting point
    queue = deque([(start, [])])
    # take note of the shortest path length
    shortest = None
    # store all the paths with the shortest path length
    res = []
    # while there are still paths to explore
    while queue:
        # get the current position and the path taken to reach the position
        current, path = queue.popleft()
        # if we have reached the end
        if current == end:
            # if we have not found the shortest path length, set it
            if shortest is None:
                shortest = len(path)
            # if the path length is the same as the shortest path length, add it to the result
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        # if we have found the shortest path length and the current path length is greater than or equal to the shortest path length, skip
        if shortest and len(path) >= shortest:
            continue
        # add all the neighbours to the queue
        for neighbour, direction in pad[current]:
            queue.append((neighbour, path + [direction]))
    return res

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
