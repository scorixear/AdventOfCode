import os, sys


with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
    text = f.read().strip()
    lines = text.split("\n")
    
    grid = []
    for line in lines:
        row = []
        for c in line:
            if c == "#":
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    
def clone_2d_array(array):
    new_array = []
    for row in array:
        new_array.append(row.copy())
    return new_array

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def get_neighbours(grid, x, y):
    neighbours = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            neighbours += grid[i][j]
    return neighbours

steps = 100
# print_grid(grid)
for i in range(steps):
    next_grid = clone_2d_array(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbours = get_neighbours(grid, x, y)
            if neighbours == 3:
                next_grid[x][y] = 1
            elif neighbours < 2 or neighbours > 3:
                    next_grid[x][y] = 0
    grid = next_grid
    # print_grid(grid)

lights_on = sum([sum(row) for row in grid])
print(lights_on)
