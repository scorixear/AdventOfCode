import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [list(line) for line in lines]
    width = len(grid[0])
    height = len(grid)
    start = (0,0)
    end = (0,0)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                start = (x, y)
            elif grid[y][x] == "E":
                end = (x, y)
    original_path = find_path(grid, start, end)
    
    counter = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "#":
                if (y > 0 and grid[y - 1][x] != "#" and y < height-1 and grid[y+1][x] != "#"):
                    counter += calculate_new_path((x, y-1), (x, y+1), original_path)
                elif(x > 0 and grid[y][x - 1] != "#" and x < width-1 and grid[y][x+1] != "#"):
                    counter += calculate_new_path((x-1, y), (x+1, y), original_path)
                    
    print(counter)
def calculate_new_path(first: tuple[int, int], second: tuple[int, int], original_path: list[tuple[int, int]]) -> int:
    first_index = original_path.index(first)
    second_index = original_path.index(second)
    path_between = second_index - first_index - 2
    if first_index > second_index:
        path_between = first_index - second_index - 2
    if path_between >= 100:
        #print(first, second, path_between)
        return 1
    return 0
    
def find_path(grid, start, finish):
    visited: set[tuple[int, int]] = set([start])
    visited_in_order = [start]
    stack = [start]
    while stack:
        x, y = stack.pop()
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and (new_x, new_y) not in visited and grid[new_y][new_x] != "#":
                if (new_x, new_y) == finish:
                    visited_in_order.append((new_x, new_y))
                    return visited_in_order
                visited.add((new_x, new_y))
                visited_in_order.append((new_x, new_y))
                stack.append((new_x, new_y))
    return visited_in_order
    
            
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
