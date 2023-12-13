import os, sys
import time

# transposes a matrix represented as a list of strings
def transpose(grid):
    new_grid = []
    for i in range(len(grid[0])):
        new_grid.append("".join([row[i] for row in grid]))
    return new_grid

# finds the vertical reflection of a grid
# by transposing the grid and finding the horizontal reflection
def find_vertical_reflection(grid):
    grid = transpose(grid)
    return find_horizontal_reflection(grid)

# finds the horizontal reflection of a grid
def find_horizontal_reflection(grid):
    # for each possible horizontal reflection
    # starting from between 0, 1
    for i in range(1, len(grid)):
        is_match = True
        # for each side of the reflection
        for j in range(1,i+1):
            # if right side is out of bounds, break
            if i+j-1 >= len(grid):
                break
            # if the sides don't match, break
            # i+j-1 is the right side, starting from i
            # i-j is the left side, starting from i-1
            if grid[i+j-1] != grid[i-j]:
                is_match = False
                break
        # if all lines matched or we broke early due to reaching the right edge
        if is_match:
            # return the index of the reflection (the first index right of the reflection)
            return i
    return 0
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grids = []
    current_grid = []
    # read in the grids
    for line in lines:
        if line == "":
            grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append(line)
    grids.append(current_grid)
    
    count = 0
    # for each grid
    for grid in grids:
        # must have either vertical or horizontal reflection
        # never has both
        result = find_vertical_reflection(grid)
        # if no vertical reflection, check for horizontal reflection
        if result == 0:
            # must find it here
            result = find_horizontal_reflection(grid)
            count += 100*result
        else:
            count += result
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
