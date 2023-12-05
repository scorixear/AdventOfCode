import os, sys, re
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()


def updateNeighbours(i, j, read, write):
  if i > 0:
    if j > 0 and read[i-1][j-1] > 0:
      write[i-1][j-1] += 1
    if read[i-1][j] > 0:
      write[i-1][j] += 1
    if j + 1 < len(read[i-1]) and read[i-1][j+1] > 0:
      write[i-1][j+1] += 1
  if j > 0 and read[i][j-1] > 0:
    write[i][j-1]+=1
  if j + 1 < len(read[i]) and read[i][j+1] > 0:
    write[i][j+1]+=1
  if i + 1 < len(read):
    if j > 0 and read[i+1][j-1] > 0:
      write[i+1][j-1] += 1
    if read[i+1][j] > 0:
      write[i+1][j] += 1
    if j + 1 < len(read[i+1]) and read[i+1][j+1] > 0:
      write[i+1][j+1] += 1

grid = []
for line in lines:
  row = []
  for char in line.strip():
    row.append(int(char))
  grid.append(row)

counter = 0
while True:
  print(counter)
  for row in grid:
    print(row)
  print("\n")
  # increase every counter
  allZero = True
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      allZero = allZero and grid[i][j] == 0
      grid[i][j] += 1
  if allZero:
    print(counter)
    break
  
  while True:
    copy = [row[:] for row in grid]
    currentFlashCount = 0
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] > 9:
          grid[i][j] = 0
          copy[i][j] = 0
          currentFlashCount+=1
          updateNeighbours(i, j, grid, copy)
   
    if currentFlashCount == 0:
      break
    grid = copy
  counter += 1