from enum import Enum
import os, sys
import time

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    @staticmethod
    def from_string(dir_type: str):
        if dir_type == "U":
            return Direction.UP
        if dir_type == "R":
            return Direction.RIGHT
        if dir_type == "D":
            return Direction.DOWN
        if dir_type == "L":
            return Direction.LEFT
        raise ValueError(f"Invalid direction type: {dir_type}")

# flood fill with a queue
def flood_fill(grid: list[list[bool]], seen: set[tuple[int, int]], x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        # extend the seen set
        if (x, y) in seen:
            continue
        # if the current grid is a border, don't extend the seen set
        if grid[y][x]:
            continue
        seen.add((x, y))
        # add all adjacent cells to the queue
        # that are not a border cell
        if x > 0 and not grid[y][x-1]:
            queue.append((x-1, y))
        if x < len(grid[0])-1 and not grid[y][x+1]:
            queue.append((x+1, y))
        if y > 0 and not grid[y-1][x]:
            queue.append((x, y-1))
        if y < len(grid)-1 and not grid[y+1][x]:
            queue.append((x, y+1))
    return seen

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    # contains all the cells that are borders
    cells = set()
    position = (0, 0)
    cells.add(position)
    # for later grid creation
    max_x, min_x = 0, 0
    max_y, min_y = 0, 0
    for line in lines:
        direction, length, _ = line.split()
        direction = Direction.from_string(direction)
        length = int(length)
        # add all cells in between to the set
        for _ in range(length):
            position = (position[0] + direction.value[0], position[1] + direction.value[1])
            # and update max and min values
            if position[0] > max_x:
                max_x = position[0]
            elif position[0] < min_x:
                min_x = position[0]
            if position[1] > max_y:
                max_y = position[1]
            elif position[1] < min_y:
                min_y = position[1]
            cells.add((position[0], position[1]))
    # offset the grid so that the top left corner is (0, 0)
    offset_x = abs(min_x)
    offset_y = abs(min_y)
    # create the grid of False values
    grid = [[False for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
    # and set all cells where there is a border to true
    for cell in cells:
        grid[cell[1]+offset_y][cell[0]+offset_x] = True
    # flood fill from all corners (might not work, but does in my case, after inspection of the created grid)
    # seen is set of all cells that are not borders and not inside the region
    seen = flood_fill(grid, set(), 0, 0)
    seen = flood_fill(grid, seen, len(grid[0])-1, 0)
    seen = flood_fill(grid, seen, 0, len(grid)-1)
    seen = flood_fill(grid, seen, len(grid[0])-1, len(grid)-1)
    # and print the number of cells that are not seen, as they are border or inside the region cells
    # only works for my input, as all out of region cells are connected to the corners of the grid
    print(len(grid)*len(grid[0]) - len(seen))
                
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
