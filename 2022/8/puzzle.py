"""provides path joining functions annd module joining"""
import os
import sys
import time

INPUT_FILE="input"

def find_edge(i,j,grid,step_i, step_j):
  init = grid[i][j]
  while True:
    i += step_i
    j += step_j
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
      break
    if grid[i][j] >= init:
      return False
  return True

def solve1(grid, height, length):
  count = 0
  for i in range(height):
    for j in range(length):
      # count edge trees
      if i == 0 or j == 0 or i == height-1 or j == length-1:
        count+=1
        continue
      if find_edge(i,j, grid, -1, 0) or find_edge(i,j,grid,1,0) or find_edge(i,j,grid,0,-1) or find_edge(i,j,grid,0,1):
        count +=1
        continue
  
  print(count)

def count_trees(i,j,grid,step_i,step_j):
  count = 0
  init = grid[i][j]
  while True:
    i += step_i
    j += step_j
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
      break
    if grid[i][j] < init:
      count+=1
    else:
      count += 1
      break
  return count

def solve2(grid, height, length):
  maxCount = 0
  for i in range(1, height-1):
    for j in range(1, length-1):
      currentCount = count_trees(i,j,grid,-1,0)*count_trees(i,j,grid,1,0)*count_trees(i,j,grid,0,-1)*count_trees(i,j,grid,0,1)
      if currentCount > maxCount:
        maxCount = currentCount
  print(maxCount)

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  height = len(lines)
  length = len(lines[0].strip())
  grid: list[list[int]] = [[0 for i in range(length)] for j in range(height)]
  
  for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
      grid[i][j] = int(char)
  
  #solve1(grid, height, length
  solve2(grid, height, length)

if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms");