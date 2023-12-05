import os, sys, time

def printGrid(grid):
  for row in grid:
    string = ""
    for cell in row:
      string += "#" if cell else "."
    print(string)

def getIndex(grid, i, j, default):
  value = 0;
  for x in range(-1, 2):
    for y in range(-1, 2):
      value <<= 1
      if i+x >= 0 and i+x < len(grid) and j+y >= 0 and j+y < len(grid[i]):
        value += grid[i+x][j+y]
      else:
        value += default
  return value

def doStep(grid, imageAlg, default):
  newGrid = [row[:] for row in grid]
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      index = getIndex(grid, i, j, default)
      newGrid[i][j] = imageAlg[index]
  return newGrid

def extendGrid(grid, number, default):
  oldLength = len(grid[0])
  for row in grid:
    for i in range(number):
      row.insert(0, default)
      row.append(default)
  grid.insert(0, [default for i in range(oldLength+number*2)])
  grid.append([default for i in range(oldLength + number*2)])

def traverseImage(grid, imageAlg):
  newGrid = doStep(grid, imageAlg, grid[0][0])
  extendGrid(newGrid, 1, newGrid[0][0])
  return newGrid

def main():
  inputText = open(os.path.join(sys.path[0], 'input'), 'r')
  lines = inputText.readlines()

  imageAlg = [char == "#" for char in lines[0].strip()]

  grid = []
  for line in lines[2:]:
    row = [char == "#" for char in line.strip()]
    grid.append(row)
  extendGrid(grid, 1, False)
  # printGrid(grid)
  for i in range(50):
    grid = traverseImage(grid, imageAlg)
    # printGrid(grid)
  counter = 0
  for row in grid:
    for cell in row:
      if cell:
        counter += 1
  print(counter)

if __name__ == "__main__":
  t = time.time()
  main()
  print (time.time() - t)