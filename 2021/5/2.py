import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

grid = {}
counter = 0
for line in lines:
    match = re.search("(\d+),(\d+) -> (\d+),(\d+)", line)
    startx, starty = int(match.group(1)), int(match.group(2))
    endx, endy = int(match.group(3)), int(match.group(4))

    if startx == endx:
        if starty > endy:
            temp = endy
            endy = starty
            starty = temp
        if startx not in grid:
            grid[startx] = {}
        for i in range(starty, endy+1):
            if i in grid[startx]:
                grid[startx][i] += 1
                if grid[startx][i] == 2:
                    counter += 1
            else:
                grid[startx][i] = 1
    elif starty == endy:
        if startx > endx:
            temp = endx
            endx = startx
            startx = temp
        for i in range(startx, endx+1):
            if i in grid:
                if starty in grid[i]:
                    grid[i][starty] += 1
                    if grid[i][starty] == 2:
                        counter += 1
                else:
                    grid[i][starty] = 1
            else:
                grid[i] = {starty: 1}
    else:
        if startx > endx:
            temp = endx
            endx = startx
            startx = temp
            temp = endy
            endy = starty
            starty = temp
        increaseY = 1
        if starty > endy:
            increaseY = -1
        for i in range(startx, endx+1):
            if i in grid:
                if starty in grid[i]:
                    grid[i][starty] += 1
                    if grid[i][starty] == 2:
                        counter += 1
                else:
                    grid[i][starty] = 1
            else:
                grid[i] = {starty: 1}
            starty += increaseY
for key in grid:
    print(key, ": ", grid[key])
print('Counter', counter)

# gridText = open(os.path.join(sys.path[0], 'grid'), 'r')
# gridLines = gridText.readlines()

# for i in range(len(gridLines)):
#     for j in range(len(gridLines[i].strip())):
#         if gridLines[i][j] == '.':
#             if (j in grid and i in grid[j]):
#                 print(i, j)
#         elif j not in grid or i not in grid[j] or int(gridLines[i][j]) != grid[j][i]:
#             print(j, i, int(gridLines[i][j]))
