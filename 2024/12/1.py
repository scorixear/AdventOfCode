import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [list(line) for line in lines]
    width = len(grid[0])
    height = len(grid)
    
    # holds all visited points
    visited_points: set[tuple[int, int]] = set()
    total = 0
    # for all points in the grid
    for y in range(height):
        for x in range(width):
            # if we already used this point in a region
            # there needs to be no bfs from this point
            if (x, y) in visited_points:
                continue
            # get the perimiter and size of the region
            perimiters, size = expand_region(grid, x, y, visited_points)
            # and sum up the result
            total += perimiters * size
    print(total)
    
def expand_region(grid: list[list[str]], x: int, y: int, visited_points: set[tuple[int, int]]):
    # normal bfs start from the current point
    stack: list[tuple[int, int]] = [(x, y)]
    # later used to determine the perimiter
    region: set[tuple[int, int]] = set([(x, y)])
    # identifing flower type, that needs to be the same in the region
    region_flower = grid[y][x]
    # we annoted this point as being visited
    visited_points.add((x, y))
    # while there are points to visit
    while stack:
        # get the next point
        x, y = stack.pop()
        # check all neighbours
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            # if the point is out of bounds, skip it
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                continue
            # if the point is not the same flower type, skip it
            if grid[new_y][new_x] != region_flower:
                continue
            # if the point was already visited, skip it
            if (new_x, new_y) in visited_points:
                continue
            # add the point to the stack and the visited points
            stack.append((new_x, new_y))
            visited_points.add((new_x, new_y))
            region.add((new_x, new_y))
    # return the size of the region and the perimiter
    return len(region), find_perimiter(region)

def find_perimiter(region: set[tuple[int, int]]):
    perimiter = 0
    # for all points in the region
    for x, y in region:
        # check all neighbours
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = x + dx, y + dy
            # if the neighbour is not in the region, it is part of the perimiter
            if (new_x, new_y) not in region:
                perimiter += 1
    return perimiter
    
            
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
