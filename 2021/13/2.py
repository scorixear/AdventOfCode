import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

gridLines = []
grid: "list[list[bool]]" =  []
swap = False
folds = []
maxX = 0
maxY = 0
for line in lines:
  if line.strip() == "":
    swap = True
    continue
  if not swap:
    coords = line.strip().split(",")

    x = int(coords[0])
    y = int(coords[1])
    if x > maxX:
      maxX = x
    if y > maxY:
      maxY = y
    gridLines.append([x,y])
  else:
    instruction = line.strip().split("=")
    folds.append([instruction[0].endswith("y"), int(instruction[1])])

for i in range(maxY + 1):
  row = []
  for j in range(maxX + 1):
    row.append(False)
  grid.append(row)

for gridLine in gridLines:
  grid[gridLine[1]][gridLine[0]] = True

def printGrid():
  for row in grid:
    rowStr = ""
    for cell in row:
      if cell:
        rowStr += "0"
      else:
        rowStr += " "
    print(rowStr)

def foldGrid(y, line):
  global grid
  global maxX
  global maxY
  if y:
    for i in range(line+1, maxY + 1):
      for j in range(maxX + 1):
        if grid[i][j]:
          newY = line - (i - line)
          grid[i][j] = False
          grid[newY][j] = True
    maxY = line
  if not y:
    for i in range(maxY + 1):
      for j in range(line + 1, maxX + 1):
        if grid[i][j]:
          newX = 2*line - j
          grid[i][j] = False
          grid[i][newX] = True
    maxX = line
  newGrid = []
  for i in range(maxY+1):
    newRow = []
    for j in range(maxX+1):
      newRow.append(grid[i][j])
    newGrid.append(newRow)
  grid = newGrid

for fold in folds:
  foldGrid(fold[0], fold[1])
printGrid()
# foldGrid(folds[0][0], folds[0][1])
# printGrid()
#print(counter)