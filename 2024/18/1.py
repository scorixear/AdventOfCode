import os, sys
import time
from dijkstra1 import Dijkstra

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    start = (0, 0)
    end = (70, 70)
    grid = [[False for _ in range(71)] for _ in range(71)]
    for i in range(1024):
        x, y = map(int, lines[i].split(","))
        grid[x][y] = True
    dijkstra = Dijkstra(lambda node: neighbour(node, grid), cost, 0)
    dijkstra.find_path(start, end)
    print(dijkstra.get_cost(end))
    
def neighbour(node: tuple[int, int], grid: list[list[bool]]):
    x, y = node
    neighbours = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and not grid[nx][ny]:
            neighbours.append((nx, ny))
    return neighbours
def cost(_: tuple[int, int], _1: tuple[int, int]):
    return 1

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")