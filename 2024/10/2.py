import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[-1 if char == "." else int(char) for char in line] for line in lines]

    start_pos: list[tuple[int, int]] = []
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 0:
                start_pos.append((x, y))
    total = 0
    for x, y in start_pos:
        total += dfs(x, y, grid, width, height)
    print(total)
def dfs(x: int, y: int, grid: list[list[int]], width: int, height: int):
    #visited = [[False for _ in range(width)] for _ in range(height)]
    hiking_paths = [[0 for _ in range(width)] for _ in range(height)]
    #visited[y][x] = True
    hiking_paths[y][x] = 1
    stack = [(x, y)]
    reached_goals = set()
    while stack:
        x, y = stack.pop()
        val = grid[y][x]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height or grid[new_y][new_x] - 1 != val:
                continue
            # visited[new_y][new_x] = True
            hiking_paths[new_y][new_x] += 1
            if grid[new_y][new_x] == 9:
                reached_goals.add((new_x, new_y))
            else:
                stack.append((new_x, new_y))
    goals = 0
    for x, y in reached_goals:
        goals += hiking_paths[y][x]
    return goals
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
