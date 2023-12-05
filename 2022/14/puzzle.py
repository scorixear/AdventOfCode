"""provides path joining functions annd module joining"""
import os
import sys
import time
from enum import Enum

class Type(Enum):
  ROCK = 0,
  SAND = 1,
  AIR = 2,
  SOURCE = 3
INPUT_FILE="input"

def type_to_string(input: Type):
  match input:
    case Type.ROCK:
      return "#"
    case Type.SAND:
      return "o"
    case Type.SOURCE:
      return "+"
    case _:
      return "."

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  lines.append("334,165 -> 666,165")
  rows = 166
  columns = 333
  #lines.append("488,11 -> 512,11")
  #rows = 12
  #columns = 25
  
  landscape = [[Type.AIR for _ in range(columns)] for _ in range(rows)]
  start = (columns//2,0)
  for line in lines:
    pairs = line.strip().split(" -> ")
    for i in range(len(pairs)-1):
      left = pairs[i]
      right = pairs[i+1]
      leftx = int(left.split(",")[0])-(500-columns//2)
      lefty = int(left.split(",")[1])
      rightx = int(right.split(",")[0])-(500-columns//2)
      righty = int(right.split(",")[1])
      if lefty > righty:
        temp = lefty
        lefty = righty
        righty = temp
      elif leftx > rightx:
        temp = leftx
        leftx = rightx
        rightx = temp
      for y in range(lefty, righty+1):
        for x in range(leftx, rightx+1):
          landscape[y][x] = Type.ROCK
  landscape[start[1]][start[0]] = Type.SOURCE
  #print_grid(landscape)
  counter = 0
  while True:
    counter+=1
    try:
      spawn_point(landscape, start)
    except NameError:
      counter += 1
      break
    except:
      break
  #print_grid(landscape)
  print(counter-1)

def print_grid(grid):
  lines = []
  for i, row in enumerate(grid):
    line = "".join(map(lambda x: type_to_string(x),row))
    lines.append(f"{line}")
  print("\n".join(lines))

def spawn_point(grid: list[list[Type]], start: tuple[int, int]):
  current_position = start
  while True:
    next_position = (current_position[0], current_position[1]+1)
    if grid[next_position[1]][next_position[0]] == Type.AIR:
      current_position = next_position
      continue
    next_position = (current_position[0]-1, current_position[1]+1)
    if grid[next_position[1]][next_position[0]] == Type.AIR:
      current_position = next_position
      continue
    next_position = (current_position[0]+1, current_position[1]+1)
    if grid[next_position[1]][next_position[0]] == Type.AIR:
      current_position = next_position
      continue
    break
  if current_position == start:
    raise NameError
  grid[current_position[1]][current_position[0]] = Type.SAND
  

if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms")