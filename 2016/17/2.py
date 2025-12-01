import heapq
import os, sys
import time
import hashlib
import itertools
moves = {
    'U': lambda x, y: (x, y-1),
    'D': lambda x, y: (x, y+1),
    'L': lambda x, y: (x-1, y),
    'R': lambda x, y: (x+1, y),
}
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")

    code = lines[0]
    start = (0,0)
    goal = (3,3)
    queue = [(start, [start], [])]
    paths = []
    while queue:
        (x, y), path, dirs = queue.pop(0)
        for dir in itertools.compress('UDLR', doors(dirs, code)):
            nx, ny = moves[dir](x, y)
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            elif (nx, ny) == goal:
                paths.append(dirs + [dir])
            else:
                queue.append(((nx, ny), path + [(nx, ny)], dirs + [dir]))
    print("Part 2:", len(paths[-1]))
                

def doors(path, code):
    string = (code + ''.join(path)).encode('utf-8')
    return (int(x, 16) > 10 for x in hashlib.md5(string).hexdigest()[:4])  

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
