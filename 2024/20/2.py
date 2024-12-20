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
    path_index: dict[tuple[int, int], int] = {}
    for i, point in enumerate(original_path):
        path_index[point] = i
    
    counter = 0
    already_checked: dict[int, set[int]] = {}
    for i, point in enumerate(original_path):
        for y in range(0, 21):
            for x in range(21 - y):
                for (dx, dy) in ((x, y), (-x, y), (x, -y), (-x, -y)):
                    
                    new_x, new_y = point[0] + dx, point[1] + dy
                    if new_x == point[0] and new_y == point[1]:
                        continue
                    new_i = path_index.get((new_x, new_y), -1)
                    if new_i == -1:
                        continue
                    if new_i in already_checked:
                        if i in already_checked[new_i]:
                            continue
                        else:
                            already_checked[new_i].add(i)
                    else:
                        already_checked[new_i] = {i}
                    if i in already_checked:
                        if new_i in already_checked[i]:
                            continue
                        else:
                            already_checked[i].add(new_i)
                    else:
                        already_checked[i] = {new_i}
                    
                    if 0 <= new_x < width and 0 <= new_y < height and grid[new_y][new_x] != "#":
                        counter += calculate_new_path(path_index[point], path_index[(new_x, new_y)], abs(new_x - point[0]) + abs(new_y - point[1]))
    print(counter)
def calculate_new_path(first_index: int, second_index: int, wall_path) -> int:
    path_between = second_index - first_index - wall_path
    if first_index > second_index:
        path_between = first_index - second_index - wall_path
    if path_between >= 100:
        return 1
    return 0

def find_path(grid, start, finish) -> list[tuple[int, int]]:
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
