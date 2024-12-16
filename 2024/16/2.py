import os, sys
import time
import enum
from dijkstra2 import Dijkstra

class Direction(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    def __hash__(self) -> int:
        return hash(self.value)
    def __lt__(self, other: "Direction") -> bool:
        return self.value < other.value
def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid: list[list[str]] = [list(line) for line in lines]
    width = len(grid[0])
    height = len(grid)
    start = (0, 0, Direction.RIGHT)
    ends = []
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                start = (x, y, Direction.RIGHT)
            elif grid[y][x] == "E":
                ends = [
                    (x, y, Direction.UP),
                    (x, y, Direction.RIGHT),
                    (x, y, Direction.DOWN),
                    (x, y, Direction.LEFT)
                ]

    dij = Dijkstra(lambda n: neighbour_func(n, grid, width, height),
                   cost_func,
                   0.0, float("inf"))
    min_cost = float("inf")
    dij.find_path(start)
    end_to_reach: tuple[int, int, Direction] | None = None
    for end in ends:
        cost =  dij.get_cost(end)
        if cost < min_cost:
            min_cost = cost
            end_to_reach = end
    known: set[tuple[int, int]] = set()
    for node in dij.get_paths(end_to_reach):
        known.add((node[0], node[1]))
    print(len(known))

def neighbour_func(
    node: tuple[int, int, Direction],
    grid: list[list[str]],
    width: int,
    height: int):
    neighbours = []
    for direction in Direction:
        if direction == node[2]:
            continue
        neighbours.append((node[0], node[1], direction))
    if node[2] == Direction.UP:
        if node[1] > 0 and grid[node[1]-1][node[0]] != "#":
            neighbours.append((node[0], node[1]-1, node[2]))
    elif node[2] == Direction.RIGHT:
        if node[0] < width-1 and grid[node[1]][node[0]+1] != "#":
            neighbours.append((node[0]+1, node[1], node[2]))
    elif node[2] == Direction.DOWN:
        if node[1] < height-1 and grid[node[1]+1][node[0]] != "#":
            neighbours.append((node[0], node[1]+1, node[2]))
    elif node[2] == Direction.LEFT:
        if node[0] > 0 and grid[node[1]][node[0]-1] != "#":
            neighbours.append((node[0]-1, node[1], node[2]))
    return neighbours
def cost_func(node1: tuple[int, int, Direction], node2: tuple[int, int, Direction]):
    if node1[0] == node2[0] and node1[1] == node2[1]:
        if node1[2] == node2[2]:
            return 0
        if node1[2] == Direction.UP or node1[2] == Direction.DOWN:
            if node2[2] == Direction.UP or node2[2] == Direction.DOWN:
                return 2000
            return 1000
        if node2[2] == Direction.UP or node2[2] == Direction.DOWN:
            return 1000
        return 2000
    return 1

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
