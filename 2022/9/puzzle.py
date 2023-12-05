"""provides path joining functions annd module joining"""
import os
import sys
import time

INPUT_FILE="input"

def no_move(head, tail):
  return abs(head[0]- tail[0]) <=1 and abs(head[1]-tail[1]) <= 1

def calc_smart(head, tail):
  if no_move(head, tail):
    return tail
  return (tail[0]+ max(min(1, head[0]-tail[0]),-1), tail[1]+max(min(1,head[1]-tail[1]),-1))

def calc_next(head, tail) -> tuple[int, int]:
  if no_move(head, tail):
    return tail
  if head[0] == tail[0]:
    if head[1] > tail[1]:
      return (tail[0], tail[1]+1)
    else:
      return (tail[0], tail[1]-1)
  elif head[1] == tail[1]:
    if head[0] > tail[0]:
      return (tail[0]+1, tail[1])
    else:
      return (tail[0]-1, tail[1])
  elif head[0] > tail[0]:
    if head[1] > tail[1]:
      return (tail[0]+1, tail[1]+1)
    else:
      return (tail[0]+1, tail[1]-1)
  else:
    if head[1] > tail[1]:
      return (tail[0]-1, tail[1]+1)
    else:
      return (tail[0]-1, tail[1]-1)

def move(direction, head, rope: list[tuple[int, int]]) -> tuple[tuple[int, int], list[tuple[int, int]]]:
  match direction:
    case 'R':
      head = (head[0]+1, head[1])
    case 'U':
      head = (head[0], head[1]+1)
    case 'L':
      head = (head[0]-1, head[1])
    case 'D':
      head = (head[0], head[1]-1)
  current_node = head
  for index, node in enumerate(rope):
    next = calc_smart(current_node, node)
    if node == next:
      break
    rope[index]= next
    current_node = rope[index]
  return (head, rope)

def print_rope(rope, head, size, start):
  grid = [['.' for _ in range(size)] for _ in range(size)]
  for i in range(1,len(rope)+1):
    node = rope[len(rope)-i]
    grid[(size-1-start[1])-node[1]][start[0]+node[0]] = str(len(rope)-i+1)
  grid[(size-1-start[1])-head[1]][start[0]+head[0]] = "H"
  for row in grid:
    print("".join(row))
    

def main():
  """Main Function called on Startup"""
  input_text= open(os.path.join(sys.path[0], INPUT_FILE),'r', encoding="UTF-8")
  lines = input_text.readlines()
  positionSet: set[tuple[int, int]] = set()
  positionSet.add((0, 0))
  headPosition = (0,0)
  rope=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
  for line in lines:
    splitted = line.split(" ")
    direction = splitted[0]
    amount = int(splitted[1].strip())
    for _ in range(amount):
      (newHead, newRope) = move(direction, headPosition, rope)
      headPosition = newHead
      rope = newRope
      positionSet.add(rope[-1])
    #print_rope(rope, headPosition, 26, (11,6))
    #print('\n')
  print(len(positionSet))
  


if __name__ == "__main__":
  st = time.time()
  main()
  et = time.time()
  evaluationtime = (et-st)*1000
  print(f"Execution time: {evaluationtime}ms");