import os, sys
import time

def get_start(grid: list[str]):
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c == "S":
                return (x,y)

def bfs(grid: list[str], start: tuple[int, int], max_steps: int):
    modulo_remainder = max_steps % 2
    reached = 0
    seen = set()
    queue = [(start, 0)]
    while queue:
        pos, steps = queue.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        x,y = pos
        if grid[y][x] == "#":
            continue
        if steps % 2 == modulo_remainder:
            reached += 1
        if steps >= max_steps:
            continue
       
        queue.append(((x+1,y), steps+1))
        queue.append(((x-1,y), steps+1))
        queue.append(((x,y+1), steps+1))
        queue.append(((x,y-1), steps+1))
    return reached

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    starting_pos = get_start(lines)
    print(bfs(lines, starting_pos, 64))
    
    
        
                
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
