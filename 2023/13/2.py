import os, sys
import time

# transposes matrix represented as list of strings
def transpose(grid):
    new_grid = []
    for i in range(len(grid[0])):
        new_grid.append("".join([row[i] for row in grid]))
    return new_grid

# finds vertical reflection of grid
# by transposing grid and finding horizontal reflection
def find_vertical_reflection(grid, vertical):
    grid = transpose(grid)
    return find_horizontal_reflection(grid, vertical)

# finds horizontal reflection of grid
def find_horizontal_reflection(grid, horizontal):
    # for each possible horizontal reflection
    for i in range(1, len(grid)):
        is_match = True
        # for each side of the reflection
        # starting at (i-1, i)
        for j in range(1,i+1):
            # if we reached the end of the grid, break
            if i+j-1 >= len(grid):
                break
            # if the sides don't match, break
            # i+j-1 is the right side, starting from i
            # i-j is the left side, starting from i-1
            if grid[i+j-1] != grid[i-j]:
                is_match = False
                break
        # if all lines matched or we broke early due to reaching the right edge
        # and this is not the same reflection as the one we found in part 1
        if is_match and i != horizontal:
            # return the index of the reflection (the first index right of the reflection)
            return i
    return 0
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grids: list[list[str]] = []
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
        # find original reflection
        vertical = find_vertical_reflection(grid, 0)
        horizontal = 0
        if vertical == 0:
            horizontal = find_horizontal_reflection(grid, 0)
        
        found_smudge = False
        # for each cell in the grid
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                # flip the cell
                new_grid = [r if y != i else row[:j] + ("#" if cell == "." else ".") + row[j+1:] for y, r in enumerate(grid)]
                # check if the new grid has different vertical reflection
                result = find_vertical_reflection(new_grid, vertical)
                # if not, check if it has different horizontal reflection
                if result == 0:
                    result = find_horizontal_reflection(new_grid, horizontal)
                    # if it does, count it
                    # otherwise continue with different smudge
                    if result != 0:
                        count += 100*result
                        found_smudge = True
                        break
                # if it does, count it
                elif result != vertical:
                    count += result
                    found_smudge = True
                    break
            # if we found a smudge, break
            if found_smudge:
                break
    print(count)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
