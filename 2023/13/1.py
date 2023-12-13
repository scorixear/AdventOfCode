import os, sys
import time

def transpose(grid):
    new_grid = []
    for i in range(len(grid[0])):
        new_grid.append("".join([row[i] for row in grid]))
    return new_grid

def find_vertical_reflection(grid):
    grid = transpose(grid)
    return find_horizontal_reflection(grid)

def find_horizontal_reflection(grid):
    for i in range(1, len(grid)):
        is_match = True
        for j in range(1,i+1):
            if i+j-1 >= len(grid):
                break
            if grid[i+j-1] != grid[i-j]:
                is_match = False
                break
        if is_match:
            return i
    return 0
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grids = []
    current_grid = []
    for line in lines:
        if line == "":
            grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append(line)
    grids.append(current_grid)
    count = 0
    for grid in grids:
        result = find_vertical_reflection(grid)
        print(result)
        if result == 0:
            result = find_horizontal_reflection(grid)
            print(result)
            count += 100*result
        else:
            count += result
        print("----")
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
